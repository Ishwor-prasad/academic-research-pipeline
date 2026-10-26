#!/usr/bin/env python3
"""
Empirical Statistical Analytics Engine for Academic Research
Performs verifiable descriptive, correlational, and inferential analyses on research datasets.
Generates publication-quality tables (CSV/Markdown) and 300 DPI graphics without data hallucination.
"""

import sys
import os
import re
import json
import argparse
from typing import Dict, List, Any

def sanitize_filename(name: str) -> str:
    clean = re.sub(r'[^a-zA-Z0-9_\-]', '_', name)
    return clean[:80].strip('_')

try:
    import numpy as np
    import pandas as pd
    from scipy import stats
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import seaborn as sns
except ImportError as e:
    sys.stderr.write(f"Error importing required scientific libraries: {e}\n")
    sys.stderr.write("Please run with uv: uv run --with pandas --with scipy --with matplotlib --with seaborn <script>\n")
    sys.exit(1)


def parse_args():
    parser = argparse.ArgumentParser(description="Empirical Statistical Analytics Engine")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: all (run complete pipeline)
    p_all = subparsers.add_parser("all", help="Execute complete descriptive, correlational, inferential, and visualization suite")
    p_all.add_argument("--dataset", required=True, help="Path to input CSV dataset")
    p_all.add_argument("--output-dir", required=True, help="Directory to save analytical outputs and figures")
    p_all.add_argument("--group-col", default=None, help="Grouping column for inferential analysis (e.g., Role)")
    p_all.add_argument("--dpi", type=int, default=300, help="Resolution for generated graphics (default: 300)")

    # Subcommand: describe
    p_desc = subparsers.add_parser("describe", help="Generate descriptive statistics and frequency distributions")
    p_desc.add_argument("--dataset", required=True, help="Path to input CSV dataset")
    p_desc.add_argument("--output-dir", required=True, help="Directory to save tables")

    # Subcommand: correlate
    p_corr = subparsers.add_parser("correlate", help="Compute correlation matrix and generate heatmap")
    p_corr.add_argument("--dataset", required=True, help="Path to input CSV dataset")
    p_corr.add_argument("--output-dir", required=True, help="Directory to save correlation results")
    p_corr.add_argument("--method", choices=["spearman", "pearson"], default="spearman", help="Correlation method")

    return parser.parse_args()


def audit_and_load(dataset_path: str) -> pd.DataFrame:
    if not os.path.exists(dataset_path):
        sys.stderr.write(f"Error: Dataset file not found at '{dataset_path}'\n")
        sys.exit(1)
    try:
        df = pd.read_csv(dataset_path)
    except Exception as e:
        sys.stderr.write(f"Error reading CSV file '{dataset_path}': {e}\n")
        sys.exit(1)

    # Basic data cleanup
    df.columns = [c.strip() for c in df.columns]
    return df


def run_descriptives(df: pd.DataFrame, out_dir: str) -> Dict[str, Any]:
    os.makedirs(out_dir, exist_ok=True)
    summary_data: Dict[str, Any] = {
        "sample_size": len(df),
        "columns": list(df.columns),
        "variables": {}
    }

    freq_tables_dir = os.path.join(out_dir, "frequency_tables")
    os.makedirs(freq_tables_dir, exist_ok=True)

    for col in df.columns:
        series = df[col].dropna()
        var_info: Dict[str, Any] = {
            "name": col,
            "count": int(len(series)),
            "missing": int(df[col].isna().sum())
        }

        # Check if numeric or convertible
        is_numeric = pd.api.types.is_numeric_dtype(series)
        if is_numeric:
            s_arr = series.values.astype(float)
            var_info["type"] = "numeric"
            var_info["mean"] = float(np.mean(s_arr))
            var_info["std"] = float(np.std(s_arr, ddof=1)) if len(s_arr) > 1 else 0.0
            var_info["median"] = float(np.median(s_arr))
            var_info["iqr"] = float(stats.iqr(s_arr)) if len(s_arr) > 1 else 0.0
            var_info["min"] = float(np.min(s_arr))
            var_info["max"] = float(np.max(s_arr))
            var_info["skewness"] = float(stats.skew(s_arr)) if len(s_arr) > 2 else 0.0
            var_info["kurtosis"] = float(stats.kurtosis(s_arr)) if len(s_arr) > 3 else 0.0
        else:
            var_info["type"] = "categorical"

        # Frequency distribution
        vc = series.value_counts()
        vp = series.value_counts(normalize=True) * 100
        freq_df = pd.DataFrame({"Count": vc, "Percentage": vp.round(2)})
        safe_name = sanitize_filename(col)
        freq_csv_path = os.path.join(freq_tables_dir, f"{safe_name}_freq.csv")
        freq_df.to_csv(freq_csv_path)

        var_info["frequencies"] = {str(k): {"count": int(v), "pct": float(round(vp[k], 2))} for k, v in vc.items()}
        summary_data["variables"][col] = var_info

    summary_file = os.path.join(out_dir, "dataset_summary.json")
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2)

    return summary_data


def run_correlations(df: pd.DataFrame, out_dir: str, method: str = "spearman", dpi: int = 300) -> pd.DataFrame:
    os.makedirs(out_dir, exist_ok=True)
    # Select numeric or ordinal columns
    num_df = df.select_dtypes(include=[np.number])
    if num_df.shape[1] < 2:
        # Try converting object columns that are ordinal or have numbers
        converted = {}
        for col in df.columns:
            try:
                converted[col] = pd.to_numeric(df[col])
            except Exception:
                pass
        if len(converted) >= 2:
            num_df = pd.DataFrame(converted)

    if num_df.shape[1] < 2:
        sys.stderr.write("Warning: Fewer than 2 numeric/ordinal variables available for correlation analysis.\n")
        return pd.DataFrame()

    corr_matrix = num_df.corr(method=method)
    corr_csv = os.path.join(out_dir, f"{method}_correlation_matrix.csv")
    corr_matrix.round(4).to_csv(corr_csv)

    # Plot Heatmap
    plt.figure(figsize=(max(8, len(corr_matrix) * 1.2), max(6, len(corr_matrix) * 1.0)))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f",
                annot_kws={"size": 10}, linewidths=0.5)
    plt.title(f"{method.capitalize()} Correlation Heatmap", fontsize=14, weight="bold", pad=12)
    plt.tight_layout()
    heatmap_path = os.path.join(out_dir, "correlation_heatmap.png")
    plt.savefig(heatmap_path, dpi=dpi)
    plt.close()

    return corr_matrix


def run_inferential(df: pd.DataFrame, group_col: str, out_dir: str) -> Dict[str, Any]:
    os.makedirs(out_dir, exist_ok=True)
    results = {}
    if not group_col or group_col not in df.columns:
        return results

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if col == group_col:
            continue
        grouped_vals = [group[col].dropna().values for _, group in df.groupby(group_col) if len(group[col].dropna()) > 0]
        if len(grouped_vals) >= 2:
            # Kruskal-Wallis
            try:
                kw_stat, kw_p = stats.kruskal(*grouped_vals)
                results[f"{col}_by_{group_col}"] = {
                    "test": "Kruskal-Wallis",
                    "statistic": float(round(kw_stat, 4)),
                    "p_value": float(round(kw_p, 4)),
                    "df": len(grouped_vals) - 1,
                    "significant_at_05": bool(kw_p < 0.05)
                }
            except Exception as e:
                pass

    out_file = os.path.join(out_dir, "inferential_test_results.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    return results


def run_visualizations(df: pd.DataFrame, out_dir: str, dpi: int = 300):
    fig_dir = os.path.join(out_dir, "figures")
    os.makedirs(fig_dir, exist_ok=True)

    sns.set_theme(style="whitegrid", palette="muted")

    for col in df.columns:
        series = df[col].dropna()
        safe_name = sanitize_filename(col)
        vc = series.value_counts()

        if len(vc) > 15:
            # High cardinality: histogram or distribution
            if pd.api.types.is_numeric_dtype(series):
                plt.figure(figsize=(8, 5))
                sns.histplot(series, kde=True, color="#2b5c8f")
                plt.title(f"Distribution of {col}", fontsize=13, weight="bold")
                plt.xlabel(col)
                plt.ylabel("Frequency")
                plt.tight_layout()
                plt.savefig(os.path.join(fig_dir, f"{safe_name}_distribution.png"), dpi=dpi)
                plt.close()
        elif 2 <= len(vc) <= 6:
            # Pie Chart
            plt.figure(figsize=(7, 7))
            colors = sns.color_palette("deep", len(vc))
            plt.pie(vc.values, labels=vc.index, autopct="%1.1f%%", startangle=140,
                    colors=colors, textprops={"fontsize": 11})
            plt.title(f"Percentage Distribution: {col}", fontsize=13, weight="bold")
            plt.tight_layout()
            plt.savefig(os.path.join(fig_dir, f"{safe_name}_pie_chart.png"), dpi=dpi)
            plt.close()
        else:
            # Bar Chart
            plt.figure(figsize=(9, 5))
            ax = sns.barplot(x=vc.values, y=[str(x) for x in vc.index], orient="h", palette="viridis")
            plt.title(f"Frequency Distribution: {col}", fontsize=13, weight="bold")
            plt.xlabel("Count (n)")
            plt.ylabel("Category")
            for p in ax.patches:
                val = int(p.get_width())
                ax.annotate(f" {val}", (p.get_x() + p.get_width(), p.get_y() + p.get_height() / 2),
                            va="center", fontsize=10)
            plt.tight_layout()
            plt.savefig(os.path.join(fig_dir, f"{safe_name}_bar_chart.png"), dpi=dpi)
            plt.close()


def main():
    args = parse_args()
    df = audit_and_load(args.dataset)

    if args.command in ["describe", "all"]:
        run_descriptives(df, args.output_dir)

    if args.command in ["correlate", "all"]:
        method = getattr(args, "method", "spearman")
        run_correlations(df, args.output_dir, method=method, dpi=getattr(args, "dpi", 300))

    if args.command in ["all"]:
        if args.group_col:
            run_inferential(df, args.group_col, args.output_dir)
        run_visualizations(df, args.output_dir, dpi=args.dpi)

    print(f"Success! Analytics generated and saved to: {args.output_dir}")


if __name__ == "__main__":
    main()

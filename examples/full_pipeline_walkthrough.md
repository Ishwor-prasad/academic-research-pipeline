# Full Pipeline Walkthrough: From Research Idea to 78-Page Monograph

This guide illustrates a complete, end-to-end execution of the `academic-research-pipeline` skill, based on the empirical study conducted on the Dhaka Stock Exchange (DSE).

---

## Step 1: Research Question & Conceptual Framework
1. **Identify the Core Topic:**
   - *Example:* "Quantitative Evaluation of Technical Trading Models and Asymmetric Downside Risk Frameworks on the Dhaka Stock Exchange."
2. **Formulate Formal Research Questions & Hypotheses:**
   - $RQ_1$: Do technical trading models generate excess returns across frontier market equity tiers?
   - $H_1$: Automated stop-loss execution significantly compresses left-tail maximum drawdown relative to unhedged momentum strategies.

---

## Step 2: Instrument Construction & Data Acquisition
1. Use `references/google_forms_script_template.js` to create the standardized questionnaire in Google Apps Script.
2. Ingest or simulate response vectors (e.g. $N=100$) into `Data sheets/dummy_data.csv`.

---

## Step 3: Empirical Statistical Computation & Visualization
Run the bundled analytics engine via `uv`:
```bash
uv run --with pandas --with scipy --with matplotlib --with seaborn \
  ~/.gemini/config/skills/academic-research-pipeline/scripts/run_statistical_analytics.py all \
  --dataset "Data sheets/dummy_data.csv" \
  --output-dir "Data Analysis" \
  --group-col "Role" \
  --dpi 300
```
**Outputs Produced:**
- `dataset_summary.json`: Ground-truth values (means, standard deviations, exact counts).
- `frequency_tables/`: Percentage distribution CSVs.
- `spearman_correlation_matrix.csv` & `correlation_heatmap.png` (300 DPI).
- `inferential_test_results.json`: Kruskal-Wallis tests and $p$-values.
- `figures/`: 300 DPI publication-ready pie charts and distribution plots.

---

## Step 4: Scaffolding and Manuscript Drafting
1. Scaffold the monograph:
```bash
uv run ~/.gemini/config/skills/academic-research-pipeline/scripts/generate_manuscript_scaffold.py \
  --title "Quantitative Evaluation of Technical Trading Models and Asymmetric Downside Risk Frameworks on the Dhaka Stock Exchange" \
  --author "Ishwor Dhungana" \
  --summary-json "Data Analysis/dataset_summary.json" \
  --output-dir "Manuscript_Package"
```
2. Author the chapters following the **Anti-Ghostwriting Protocol**:
   - Every number in the results section must cite `dataset_summary.json`.
   - Embed figures from `figures/` using `\includegraphics`.
   - Add verified BibTeX records to `references.bib`.

---

## Step 5: Verification & Quality Assurance
Run the integrity verification auditor:
```bash
uv run ~/.gemini/config/skills/academic-research-pipeline/scripts/verify_academic_integrity.py \
  --manuscript "Manuscript_Package/main.tex" \
  --bib "Manuscript_Package/references.bib" \
  --summary-json "Data Analysis/dataset_summary.json" \
  --output-report "Manuscript_Package/Manuscript_Quality_Check.md"
```
Ensure all verification checks pass before compiling into PDF via `pdflatex` or `tectonic`.

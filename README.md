# Academic Research Pipeline: AI Empirical Co-Pilot

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Anti-Ghostwriting Protocol](https://img.shields.io/badge/Academic%20Integrity-Zero%20Ghostwriting-green.svg)](references/anti_ghostwriting_protocol.md)
[![LaTeX & Typst](https://img.shields.io/badge/Typesetting-LaTeX%20%7C%20Typst-teal.svg)](references/latex_templates/)

An end-to-end, scientifically defensible **Academic Research & Publication Pipeline** skill for AI coding assistants (Google Antigravity, Gemini CLI, Claude Code, Codex).

This skill transitions AI from a generic text generator into a rigorous **Empirical Research Co-Pilot**. It guides research scholars through the entire lifecycle—from literature framing and survey design to automated statistical computation, 300 DPI visualizations, and publication-ready 40+ page LaTeX/Typst monographs.

---

## 🛡️ Anti-Ghostwriting & Zero-Fabrication Philosophy

Under international publication ethics (COPE / ICMJE):
- **Zero Numerical Fabrication:** The AI agent never invents or hallucinates descriptive statistics, sample sizes, survey distributions, or $p$-values. Every single number reported in the text is computed directly on raw data files by reproducible Python scripts.
- **Zero Hallucinated Citations:** Every citation must be authentic and verified against scholarly databases (OpenAlex, Europe PMC, PubMed, arXiv). Fictitious author papers are strictly forbidden.
- **Human Author Ownership:** The researcher owns the intellectual thesis, hypotheses, and theoretical conclusions. Unverified assumptions or missing details are explicitly tagged with `[Author verification required]` rather than filled with AI guesswork.

---

## 🚀 Global Installation

### Option 1: Global Install for Google Antigravity (Recommended)
Clone directly into your global Antigravity skills directory so it is available across **all** your projects and workspaces:

```bash
git clone https://github.com/Ishwor-prasad/academic-research-pipeline.git ~/.gemini/config/skills/academic-research-pipeline
```
*(On Windows PowerShell)*:
```powershell
git clone https://github.com/Ishwor-prasad/academic-research-pipeline.git "$env:USERPROFILE\.gemini\config\skills\academic-research-pipeline"
```

### Option 2: Project-Local Install
Install inside an individual research repository:
```bash
git clone https://github.com/Ishwor-prasad/academic-research-pipeline.git .agents/skills/academic-research-pipeline
```

---

## 📂 Architecture & Directory Structure

```
academic-research-pipeline/
├── SKILL.md                               # Master protocol and agent instructions
├── README.md                              # Public documentation and installation guide
├── LICENSE                                # MIT License
├── references/
│   ├── anti_ghostwriting_protocol.md      # Strict ethical boundaries & verification criteria
│   ├── statistical_analysis_standards.md  # APA 7th reporting standards & non-parametric rules
│   ├── google_forms_script_template.js    # Automated survey generator for Google Apps Script
│   ├── latex_templates/
│   │   ├── monograph_master.tex           # 40+ page IMRaD monograph template with booktabs
│   │   └── references_template.bib        # Verified BibTeX schema
│   └── typst_templates/
│       └── methodology_template.typ       # Concise Typst methodology template
├── scripts/
│   ├── run_statistical_analytics.py       # Standalone CLI for descriptive, correlational, & inferential analysis
│   ├── generate_manuscript_scaffold.py    # Auto-scaffolds LaTeX/Typst papers from data summary
│   └── verify_academic_integrity.py       # Automated auditor checking data consistency & 0 broken citations
└── examples/
    └── full_pipeline_walkthrough.md       # Step-by-step example from CSV to 78-page compiled PDF
```

---

## ⚡ Quick Start & Usage

### 1. Run Empirical Analytics
Analyze any survey or quantitative dataset (`data.csv`):
```bash
uv run --with pandas --with scipy --with matplotlib --with seaborn \
  scripts/run_statistical_analytics.py all \
  --dataset "path/to/data.csv" \
  --output-dir "Data_Analysis" \
  --group-col "Role" \
  --dpi 300
```
This generates:
- `dataset_summary.json`: Ground-truth values (means, std, counts, skewness, kurtosis).
- `frequency_tables/`: Percentage distribution CSVs.
- `spearman_correlation_matrix.csv` & `correlation_heatmap.png`.
- `figures/`: Publication-grade (300 DPI) pie charts and distribution plots.

### 2. Scaffold Monograph
Generate a publication structure linked directly to your empirical variables:
```bash
uv run scripts/generate_manuscript_scaffold.py \
  --title "Empirical Investigation of Quantitative Trading Models" \
  --author "Lead Researcher" \
  --summary-json "Data_Analysis/dataset_summary.json" \
  --output-dir "Manuscript"
```

### 3. Verify Academic Integrity (Anti-Ghostwriting Audit)
Verify that in-text claims match your data and zero citations are broken:
```bash
uv run scripts/verify_academic_integrity.py \
  --manuscript "Manuscript/main.tex" \
  --bib "Manuscript/references.bib" \
  --summary-json "Data_Analysis/dataset_summary.json" \
  --output-report "Manuscript_Quality_Check.md"
```

---

## 📖 Citation & Ethics

If you use this pipeline in your empirical publications, please cite or reference the repository:

```bibtex
@software{Dhungana2026AcademicPipeline,
  author    = {Dhungana, Ishwor},
  title     = {Academic Research Pipeline: AI Empirical Co-Pilot and Publication Engine},
  year      = {2026},
  publisher = {GitHub},
  url       = {https://github.com/Ishwor-prasad/academic-research-pipeline}
}
```

## License
MIT License. Free for academic, scientific, and commercial research.

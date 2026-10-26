# Anti-Ghostwriting & Academic Integrity Protocol

## 1. Guiding Principle: AI as Co-Pilot, Not Ghostwriter

The purpose of the `academic-research-pipeline` skill is to elevate human scholarship through rigorous methodological assistance, reproducible computation, and publication-standard typesetting—**not** to replace the researcher's intellectual ownership or invent ungrounded scholarship.

Under international academic publication ethics (COPE, ICMJE):
- **Ghostwriting** is defined as generating unverified academic manuscripts, fabricating empirical evidence or literature, or presenting automated AI output as unreviewed empirical work without human validation.
- **Ethical AI Assistance** provides computational execution, reproducible statistical testing, literature search structuring, and formal academic drafting grounded 100% in verified data and sources.

---

## 2. The Four Non-Negotiable Tenets

### Tenet 1: Zero Numerical Fabrication
- **Rule:** The AI agent must NEVER invent, approximate, or estimate descriptive statistics, survey frequencies, percentages, test statistics ($t$, $F$, $H$, $\chi^2$, $z$), degrees of freedom ($df$), or $p$-values.
- **Enforcement:** Every number reported in the text, tables, and figures MUST be programmatically extracted from the raw dataset using `run_statistical_analytics.py` or verifiable Python scripts. If an analysis was not run, it must not be reported.

### Tenet 2: Zero Hallucinated Citations
- **Rule:** The AI agent must NEVER invent fictitious authors, speculative journal titles, fake publication years, or invalid DOIs.
- **Enforcement:** Every citation must be verified against actual scholarly indexing services (e.g., OpenAlex, Europe PMC, PubMed, arXiv, CrossRef) or provided source files. BibTeX entries must contain real bibliographic keys and metadata.

### Tenet 3: Researcher-Owned Thesis & Hypotheses
- **Rule:** The human researcher is the intellectual author of the research questions ($RQ$), directional hypotheses ($H$), and the core conceptual framework.
- **Enforcement:** The AI assists by formally structuring hypotheses and defining operational variables, but must never invent arbitrary findings to confirm a hypothesis. If the empirical data yields $p > 0.05$ (fail to reject null), the manuscript must transparently report the non-significant result and discuss its theoretical implications honestly.

### Tenet 4: Explicit Labeling of Missing Data or Unverified Assumptions
- **Rule:** When background details (such as sample demographics, specific institutional approvals, or instrument validation procedures) are not present in the workspace, the AI must NOT fabricate them.
- **Enforcement:** The AI must explicitly mark missing items with `[Author verification required: <specific question>]` so the human author provides the authentic details before journal submission.

---

## 3. Manuscript Quality Checklist (Audit Standard)

Before any manuscript is considered complete, the following checklist must be validated:

- [ ] **Data Audit:** Dataset has been checked for missing values, range bounds, and variable types.
- [ ] **Exact Value Consistency:** In-text figures match table values, which match the output of `run_statistical_analytics.py`.
- [ ] **Citation Traceability:** Every in-text `\cite{}` / `\citep{}` resolves to an authentic entry in `references.bib`.
- [ ] **Visual Integrity:** All figures (charts, heatmaps, distributions) are generated at $\ge 300\text{ DPI}$ with explicit units, labels, and informative captions.
- [ ] **Transparent Limitations:** The paper includes a dedicated Limitations section detailing sample size constraints, potential selection biases, and boundaries of generalizability.

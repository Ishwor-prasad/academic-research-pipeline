# Statistical Analysis & Academic Reporting Standards

## 1. Decision Matrix: Parametric vs. Non-Parametric Tests

Before selecting any statistical procedure, verify normality (Shapiro-Wilk test or skewness/kurtosis bounds: $|\text{skew}| < 2$, $|\text{kurtosis}| < 7$) and measurement scale:

| Research Objective | Parametric (Normal Continuous) | Non-Parametric (Ordinal / Skewed) | Categorical / Nominal |
| :--- | :--- | :--- | :--- |
| **Comparing 2 Independent Groups** | Independent Samples $t$-test | Mann-Whitney $U$ test | Chi-Square Test ($\chi^2$) |
| **Comparing $\ge 3$ Independent Groups** | One-Way ANOVA ($F$-test) | Kruskal-Wallis $H$-test | Contingency Cross-tabulation |
| **Assessing Bivariate Association** | Pearson Correlation ($r$) | Spearman Rank Correlation ($\rho$) | Cramér's $V$ / Phi ($\phi$) |
| **Predicting Continuous Outcome** | OLS Multiple Linear Regression | Robust Regression / Quantile Reg | Logistic Regression (Binary) |

---

## 2. APA 7th Statistical Notation Standards

When reporting statistical results in the text or table notes, adhere to standard formatting:
- Italicize statistical symbols: $N$, $M$, $SD$, $p$, $t$, $F$, $H$, $r$, $\rho$, $df$, $\chi^2$, $R^2$.
- Report exact $p$-values to two or three decimal places:
  - Example: $p = 0.024$, $p = 0.622$.
  - If $p < 0.001$, report as $p < .001$ (never $p = 0.000$).
- Always report effect sizes or central tendencies alongside test statistics:
  - Parametric: $M = 3.42$, $SD = 1.12$, $t(98) = 2.45$, $p = .016$, Cohen's $d = 0.49$.
  - Non-parametric: Median $= 3.00$, $IQR = 1.50$, $H(3) = 1.77$, $p = .622$.

---

## 3. Standard Table Presentation Rules

1. **Three-Rule Line Structure:** Academic tables should use booktabs horizontal lines only:
   - `\toprule` above column headers.
   - `\midrule` below column headers.
   - `\bottomrule` at the end of the data rows.
   - Avoid vertical lines in publication tables.
2. **Explanatory Notes:** Always include a `\item Note.` below the table defining abbreviations, sample size ($N = 100$), and significance asterisks ($^*p < .05, ^{**}p < .01, ^{***}p < .001$).
3. **Data Completeness:** Every percentage table must report both raw counts ($n$) and relative frequencies ($\%$), summing cleanly to 100%.

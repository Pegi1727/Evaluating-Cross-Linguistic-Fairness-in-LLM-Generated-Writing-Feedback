
# Evaluating Cross-Linguistic Fairness in LLM-Generated Writing Feedback using the Multilingual Feedback Fairness Index (MFFI)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21440273.svg)](https://doi.org/10.5281/zenodo.21440273)
[![Release](https://img.shields.io/badge/release-v1.0.0.cr-blue.svg)](https://github.com/Pegi1727/Evaluating-Cross-Linguistic-Fairness-in-LLM-Generated-Writing-Feedback/releases)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.2%2B-276DC3.svg)](https://www.r-project.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Overview & Key Visualizations

This repository contains the official dataset, statistical scripts (Python & R), and replication materials for the study: **"Evaluating Cross-Linguistic Fairness in LLM-Generated Writing Feedback using the Multilingual Feedback Fairness Index (MFFI)"**.

The study investigates systematic disparities in feedback quality across diverse First Language (L1) backgrounds (Persian, Spanish, Arabic, Chinese), evaluates model performance (GPT-4o, Claude, Gemini 2.5), and demonstrates how fairness-aware prompt engineering mitigates cross-linguistic biases.

---

### 📊 Figures & Visual Analysis

<div align="center">

#### Figure 1: Feedback Quality Across LLMs and Prompt Strategies
<img src="figures/fig1_model_prompt.png" alt="Overall Score by Model and Prompt" width="85%"/>

*Figure 1: Overall feedback score distribution across LLM architectures (GPT-4o, Claude, Gemini 2.5) conditioned on Baseline vs. Fairness-Aware Prompting.*

---

#### Figure 2: Cross-Linguistic Fairness Across Learner L1 Backgrounds
<img src="figures/fig2_fairness_L1.png" alt="Fairness Across L1 Groups" width="85%"/>

*Figure 2: Performance disparity across L1 groups (Persian, Spanish, Arabic, Chinese) and the gap-reduction effect introduced by fairness-aware instructions.*

---

#### Figure 3: Pearson Correlation Heatmap of Quality Dimensions
<img src="figures/fig3_corr_heatmap.png" alt="Correlation Heatmap" width="75%"/>

*Figure 3: Inter-metric correlation matrix highlighting relationships between Feedback Quality Index (FQI), Human Ratings, Specificity, and Pedagogical Tone.*

---

#### Figure 4 & 5: Human Validation and Proficiency Stratification
| Figure 4: Human vs. LLM Overall Score | Figure 5: Overall Score by CEFR Proficiency |
| :---: | :---: |
| <img src="figures/fig4_human_vs_overall.png" alt="Human vs Overall Score" width="100%"/> | <img src="figures/fig5_cefr_box.png" alt="CEFR Boxplot" width="100%"/> |
| *Correlation & alignment between expert human evaluations and automated scores.* | *Score distribution across CEFR language proficiency levels (A1–C2).* |

</div>

---

## 📈 Key Statistical Findings

### 1. Model & L1 Benchmark Summary

| Model / Group | Overall Score (Mean ± SD) | Human Score | Baseline MFFI | Fairness-Aware MFFI | Δ Fairness Index |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **GPT-4o** | **4.346 ± 0.38** | 3.956 | 0.92 | **0.95** | +0.03 ($p < .001$) |
| **Claude** | 4.097 ± 0.42 | 3.707 | 0.88 | **0.92** | +0.04 ($p < .001$) |
| **Gemini 2.5** | 3.802 ± 0.51 | 3.409 | 0.83 | **0.89** | **+0.06** ($p < .001$) |
| **Persian L1** | **4.248** | 3.898 | — | — | Baseline Ref |
| **Spanish L1** | 4.180 | 3.812 | — | — | $\Delta = -0.02$ ($n.s.$) |
| **Arabic L1** | 4.044 | 3.654 | — | — | $\Delta = -0.08$ ($p = .012$) |
| **Chinese L1** | **3.864** | 3.361 | — | — | $\Delta = -0.14$ ($p < .001$) |

### 2. One-Way ANOVA across L1 Groups

| Feedback Dimension | $F$-statistic | $p$-value | Partial $\eta^2$ | Disparity Level |
| :--- | :---: | :---: | :---: | :---: |
| **Specificity** | **28.64** | **< .001** | **.14** | High Disparity |
| **Actionability** | **24.92** | **< .001** | **.13** | High Disparity |
| **Accuracy** | 21.87 | < .001 | .10 | Moderate Disparity |
| **Pedagogical Appropriateness** | 19.08 | < .001 | .10 | Moderate Disparity |
| **Helpfulness** | 17.54 | < .001 | .09 | Moderate Disparity |
| **Socio-Affective Tone** | 7.21 | < .01 | .04 | Low Disparity |

### 3. Mixed-Effects & OLS Regression (Dependent Variable: `Overall_Score`)

$$\text{Overall\_Score} = \beta_0 + \beta_1(\text{Model}) + \beta_2(\text{L1}) + \beta_3(\text{Prompt}) + \beta_4(\text{CEFR}) + \epsilon$$

- **Fairness-Aware Prompting:** $\beta = +0.08$, $SE = 0.02$, $t = 4.21$, $p < .001$ *(Significant overall bias reduction)*
- **Chinese L1 Disparity:** $\beta = -0.14$, $SE = 0.03$, $t = -4.66$, $p < .001$ *(Baseline gap against Persian/Spanish)*
- **CEFR Level:** $\beta = +0.21$, $SE = 0.03$, $t = 7.00$, $p < .001$ *(Higher proficiency receives more coherent feedback)*

---

## 🔬 Key Conclusions

1. **Systematic L1 Disparities Exist:** LLM writing feedback models exhibit measurable unfairness across L1 backgrounds. Chinese and Arabic L1 essays experience higher error-density penalties and lower specificity ratings compared to Indo-European / Persian counterparts.
2. **Fairness-Aware Prompt Engineering Works:** Introducing explicit sociolinguistic and cross-linguistic constraints into LLM prompts reduces the cross-linguistic performance gap significantly (up to $\Delta = +0.06$ MFFI improvement in Gemini 2.5).
3. **Metric Alignment:** Automated Feedback Quality Index (FQI) scores strongly align with expert human evaluator ratings ($r > 0.82$), validating MFFI as a standard benchmark for pedagogical NLP fairness.

---
📜 Citation
If you find this dataset, code, or methodology helpful in your research, please cite:

bibtex
@misc{merrikhi2026evaluating,
  author       = {Merrikhi, Pegah},
  title        = {{Evaluating Cross-Linguistic Fairness in LLM-Generated Writing Feedback using the Multilingual Feedback Fairness Index (MFFI)}},
  year         = {2026},
  version      = {v1.0.0.cr},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.21440273},
  url          = {https://doi.org/10.5281/zenodo.21440273}
}
---

📄 License
This repository is distributed under the MIT License. See LICENSE for complete terms.

---
## 📁 Repository Structure
```text
Evaluating-Cross-Linguistic-Fairness-in-LLM-Generated-Writing-Feedback/
├── data/
│   └── Fairness_Full_Dataset.csv          # Full experimental dataset (24,000 observations)
├── figures/                               # Publication-ready figures (300 DPI)
│   ├── fig1_model_prompt.png
│   ├── fig2_fairness_L1.png
│   ├── fig3_corr_heatmap.png
│   ├── fig4_human_vs_overall.png
│   └── fig5_cefr_box.png
├── notebooks/                             # Interactive Jupyter Notebooks
│   ├── 01_Statistical_Analysis_Benchmark.ipynb
│   └── 02_Explainable_AI_SHAP_Analysis.ipynb
├── results/                               # Statistical outputs & summary tables
│   ├── statistical_tests/
│   └── Fairness_Analysis_Results.xlsx
├── scripts/                               # Executable analysis pipelines (Python & R)
│   ├── 01_statistical_analysis.R
│   ├── 02_regression_and_correlation.R
│   ├── 03_plots.R
│   └── run_analysis.py
├── LICENSE                                # MIT License
├── README.md                              # Main documentation
└── Requirements.text                      # Environment dependencies

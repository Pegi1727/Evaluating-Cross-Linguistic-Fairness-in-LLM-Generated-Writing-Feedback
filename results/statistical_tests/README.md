# Statistical Tests

This directory stores the raw output logs from inferential statistical analyses used to validate the paper's hypotheses.

## Contents
- `Table_2_MANOVA.txt`: Multivariate Analysis of Variance results examining the effect of L1 on feedback metrics.
- `Table_4_Tukey_HSD.txt`: Post-hoc Tukey HSD pairwise comparison results for L1 groups.

## Usage
These files are the primary record of the statistical significance tests. If you perform additional tests (e.g., regressions or ANOVA), append their outputs here.
# Analysis Tables

This directory contains aggregated numerical data tables used in the manuscript, supplementary materials, and reporting.

## Contents
- `fqi_by_model_prompt.csv`: Aggregated Feedback Quality Index (FQI) scores.
- `mfi_by_l1_model_prompt.csv`: Multilingual Fairness Index (MFI) values.
- `descriptive_statistics.csv`: Summary statistics (Mean, SD, N) for all evaluation dimensions.
- `groupwise_score_summary.csv`: Aggregated performance by demographic metadata.

## Usage
These tables are generated programmatically by the scripts in `src/` and are intended for direct use in the manuscript's result sections.
# Figures

This directory stores publication-ready visualizations generated from the dataset.

## Contents
- `figure_1_model_comparison.png`: Overall model performance comparison.
- `figure_2_prompt_effect.png`: Baseline vs. Fairness-Aware prompt analysis.
- `figure_3_l1_fairness_distribution.png`: Performance spread across L1 groups.
- `figure_4_mfi_heatmap.png`: Visualization of multilingual fairness patterns.
# Process Logs

This directory contains logs documenting the data processing and analysis pipeline.

## Contents
- `preprocessing_log.txt`: Documentation of data cleaning, imputation, and feature engineering steps.
- `analysis_log.txt`: Execution logs from statistical analysis, including model configurations and software versions.

## Importance
These logs ensure the transparency and reproducibility of the research. Please refer to these files if debugging inconsistencies in the output tables or figures.

## Reproducibility
Figures should be regenerated from the source data via `notebooks/04_visualization.ipynb` to ensure consistency with any updates to the dataset.

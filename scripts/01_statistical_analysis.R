# ==============================================================================
# Script: 01_statistical_analysis.R
# Project: Cross-Linguistic Fairness in LLM Written Feedback
# Author: Pegah Merrikhi
# Description: Descriptive statistics, ANOVA, non-parametric tests, and Cohen's d
# ==============================================================================

# 1. Load Required Packages
suppressPackageStartupMessages({
  library(tidyverse)
  library(rstatix)
  library(ez)
  library(effectsize)
  library(writexl)
})

# Create output directories if they don't exist
dir.create("analysis_outputs_r", showWarnings = FALSE)
dir.create("analysis_outputs_r/figures", showWarnings = FALSE)

# 2. Read Dataset & Preprocessing
df <- read.csv("Fairness_Full_Dataset.csv", stringsAsFactors = FALSE)

# Convert categorical variables to factors
df <- df %>%
  mutate(
    Model = factor(Model, levels = c("GPT-4o", "Claude 4", "Gemini 2.5")),
    Prompt = factor(Prompt, levels = c("Baseline", "FairnessAware")),
    L1 = factor(L1, levels = c("Persian", "Arabic", "Chinese", "Spanish")),
    CEFR = factor(CEFR, levels = c("B1", "B2", "C1"))
  )

# Calculate Feedback Quality Index (FQI)
qual_cols <- c("Accuracy", "Helpfulness", "Specificity", 
               "Actionability", "Pedagogical_Appropriateness", "Socio_Affective_Tone")
df$FQI <- rowMeans(df[, qual_cols], na.rm = TRUE)

cat("Dataset shape: ", nrow(df), "rows and", ncol(df), "columns.\n")

# 3. Descriptive Statistics
descriptive_summary <- df %>%
  group_by(Model, Prompt, L1) %>%
  summarise(
    N = n(),
    Overall_Mean = mean(Overall_Score, na.rm = TRUE),
    Overall_SD   = sd(Overall_Score, na.rm = TRUE),
    FQI_Mean     = mean(FQI, na.rm = TRUE),
    FQI_SD       = sd(FQI, na.rm = TRUE),
    Human_Mean   = mean(Human_Score, na.rm = TRUE),
    Human_SD     = sd(Human_Score, na.rm = TRUE),
    .groups = "drop"
  )

write.csv(descriptive_summary, "analysis_outputs_r/01_Descriptive_Statistics.csv", row.names = FALSE)
cat("Descriptive statistics saved successfully.\n")

# 4. Prompt Effect Analysis (Baseline vs. FairnessAware)
paired_data <- df %>%
  select(Essay_ID, Model, L1, Prompt, Overall_Score) %>%
  pivot_wider(names_from = Prompt, values_from = Overall_Score)

# Paired t-test and Wilcoxon signed-rank test
ttest_res <- t.test(paired_data$FairnessAware, paired_data$Baseline, paired = TRUE)
wilcox_res <- wilcox.test(paired_data$FairnessAware, paired_data$Baseline, paired = TRUE)
cohen_res <- cohens_d(paired_data$FairnessAware, paired_data$Baseline, paired = TRUE)

prompt_effect_df <- data.frame(
  Comparison = "FairnessAware vs Baseline",
  Mean_Baseline = mean(paired_data$Baseline, na.rm = TRUE),
  Mean_FairnessAware = mean(paired_data$FairnessAware, na.rm = TRUE),
  Mean_Diff = mean(paired_data$FairnessAware - paired_data$Baseline, na.rm = TRUE),
  t_statistic = ttest_res$statistic,
  df = ttest_res$parameter,
  p_value_ttest = ttest_res$p.value,
  wilcox_V = wilcox_res$statistic,
  p_value_wilcox = wilcox_res$p.value,
  cohens_d = cohen_res$Cohens_d
)

write.csv(prompt_effect_df, "analysis_outputs_r/02_Prompt_Effect_Paired.csv", row.names = FALSE)
cat("Prompt Effect analysis complete.\n")

# 5. Two-Way ANOVA (Model x L1)
anova_model <- aov(Overall_Score ~ Model * L1, data = df)
anova_summary <- summary(anova_model)
eta_sq <- eta_squared(anova_model, partial = FALSE)

cat("\n--- Two-Way ANOVA Summary ---\n")
print(anova_summary)

write.csv(as.data.frame(anova_summary[[1]]), "analysis_outputs_r/03_TwoWay_ANOVA.csv")
write.csv(as.data.frame(eta_sq), "analysis_outputs_r/04_ANOVA_Eta_Squared.csv", row.names = FALSE)

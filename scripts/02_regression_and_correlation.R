# ==============================================================================
# Script: 02_regression_and_correlation.R
# Project: Cross-Linguistic Fairness in LLM Written Feedback
# Author: Pegah Merrikhi
# Description: OLS Regression, VIF analysis, Pearson/Spearman Correlations
# ==============================================================================

library(tidyverse)
library(car)

# Load data
df <- read.csv("Fairness_Full_Dataset.csv")

qual_cols <- c("Accuracy", "Helpfulness", "Specificity", 
               "Actionability", "Pedagogical_Appropriateness", "Socio_Affective_Tone")
df$FQI <- rowMeans(df[, qual_cols], na.rm = TRUE)

# 1. OLS Multiple Linear Regression Model
ols_fit <- lm(Overall_Score ~ factor(Model) + factor(Prompt) + factor(L1) + 
                factor(CEFR) + Error_Density + Lexical_Sophistication, data = df)

sink("analysis_outputs_r/05_OLS_Regression_Summary.txt")
cat("==================================================================\n")
cat("   OLS REGRESSION SUMMARY FOR OVERALL FEEDBACK SCORE (R)          \n")
cat("==================================================================\n\n")
print(summary(ols_fit))
cat("\n--- Variance Inflation Factor (VIF) ---\n")
print(vif(ols_fit))
sink()

cat("Regression model fitted. Summary exported to txt.\n")

# 2. Pearson and Spearman Correlation Matrices
numeric_vars <- df %>% select(Overall_Score, FQI, Human_Score, Accuracy, Helpfulness, Specificity, Error_Density, Lexical_Sophistication)

pearson_matrix <- cor(numeric_vars, method = "pearson", use = "complete.obs")
spearman_matrix <- cor(numeric_vars, method = "spearman", use = "complete.obs")

write.csv(pearson_matrix, "analysis_outputs_r/06_Correlation_Pearson.csv")
write.csv(spearman_matrix, "analysis_outputs_r/07_Correlation_Spearman.csv")

# 3. Human Agreement & Correlation by Prompt Type
agreement_by_prompt <- df %>%
  group_by(Prompt) %>%
  summarise(
    Pearson_r = cor(Overall_Score, Human_Score, method = "pearson"),
    Spearman_rho = cor(Overall_Score, Human_Score, method = "spearman"),
    MAE = mean(abs(Overall_Score - Human_Score)),
    RMSE = sqrt(mean((Overall_Score - Human_Score)^2))
  )

write.csv(agreement_by_prompt, "analysis_outputs_r/08_Human_Agreement_by_Prompt.csv", row.names = FALSE)
cat("Human agreement analysis finished successfully.\n")

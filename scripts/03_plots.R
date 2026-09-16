# ==============================================================================
# Script: 03_plots.R
# Project: Cross-Linguistic Fairness in LLM Written Feedback
# Author: Pegah Merrikhi
# Description: High-resolution publication-ready visualizations via ggplot2
# ==============================================================================

library(tidyverse)
library(ggpubr)
library(corrplot)

df <- read.csv("Fairness_Full_Dataset.csv")

# Set theme
theme_set(theme_bw(base_size = 14))

# Figure 1: Model x Prompt Overall Score
p1 <- ggplot(df, aes(x = Model, y = Overall_Score, fill = Prompt)) +
  geom_boxplot(outlier.alpha = 0.3) +
  scale_fill_manual(values = c("#E69F00", "#56B4E9")) +
  labs(title = "Overall Feedback Score by Model and Prompt",
       x = "LLM Architecture", y = "Overall Score (1-5)")

ggsave("analysis_outputs_r/figures/fig1_model_prompt_r.png", plot = p1, width = 8, height = 6, dpi = 300)

# Figure 2: Fairness across L1 Backgrounds
p2 <- ggplot(df, aes(x = L1, y = Overall_Score, fill = Prompt)) +
  geom_boxplot(outlier.shape = NA) +
  scale_fill_manual(values = c("#D55E00", "#009E73")) +
  labs(title = "Cross-Linguistic Bias Reduction by Prompt Type",
       x = "Learner L1 Background", y = "Overall Feedback Score")

ggsave("analysis_outputs_r/figures/fig2_fairness_L1_r.png", plot = p2, width = 9, height = 6, dpi = 300)

# Figure 3: Human vs Model Overall Score Scatter Plot
p3 <- ggplot(df, aes(x = Human_Score, y = Overall_Score, color = Model)) +
  geom_jitter(alpha = 0.2) +
  geom_smooth(method = "lm", se = FALSE, size = 1.2) +
  labs(title = "Human Assessment vs. LLM Overall Score",
       x = "Human Score", y = "LLM Feedback Score")

ggsave("analysis_outputs_r/figures/fig4_human_vs_overall_r.png", plot = p3, width = 8, height = 6, dpi = 300)

cat("All R figures generated successfully in analysis_outputs_r/figures/\n")

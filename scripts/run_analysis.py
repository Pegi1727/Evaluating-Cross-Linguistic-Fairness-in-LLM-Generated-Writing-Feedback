import os
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

# Create directories
os.makedirs("analysis_outputs/figures", exist_ok=True)

# Load data
df = pd.read_csv("Fairness_Full_Dataset.csv")

# Compute Feedback Quality Index (FQI)
qual_cols = ['Accuracy', 'Helpfulness', 'Specificity', 'Actionability', 'Pedagogical_Appropriateness', 'Socio_Affective_Tone']
df['FQI'] = df[qual_cols].mean(axis=1)

# Excel Writer setup
excel_path = "analysis_outputs/Fairness_Analysis_Results.xlsx"
writer = pd.ExcelWriter(excel_path, engine='openpyxl')

# 1. Structure
df_struct = pd.DataFrame({
    'Metric': ['Total Rows', 'Columns'],
    'Value': [df.shape[0], df.shape[1]]
})
df_struct.to_excel(writer, sheet_name='01_Structure', index=False)

# 2. Descriptives
desc_overall = df.groupby(['Model', 'Prompt', 'L1'])[['Overall_Score', 'FQI', 'Human_Score']].agg(['mean', 'std', 'min', 'max'])
desc_overall.to_excel(writer, sheet_name='03_Descriptives')

# 3. Prompt Effect (Paired T-Test)
base_scores = df[df['Prompt'] == 'Baseline']['Overall_Score'].values
fair_scores = df[df['Prompt'] == 'FairnessAware']['Overall_Score'].values

t_stat, p_val_t = stats.ttest_rel(fair_scores, base_scores)
wilc_stat, p_val_w = stats.wilcoxon(fair_scores, base_scores)
cohen_d = (np.mean(fair_scores) - np.mean(base_scores)) / np.std(fair_scores - base_scores)

prompt_res = pd.DataFrame([{
    'Metric': 'Baseline vs FairnessAware',
    'Mean_Baseline': np.mean(base_scores),
    'Mean_FairnessAware': np.mean(fair_scores),
    'Mean_Diff': np.mean(fair_scores) - np.mean(base_scores),
    't_stat': t_stat,
    'p_val_ttest': p_val_t,
    'wilcoxon_stat': wilc_stat,
    'p_val_wilcoxon': p_val_w,
    'cohen_d': cohen_d
}])
prompt_res.to_excel(writer, sheet_name='11_Prompt_Effect_Paired', index=False)

# 4. Two-Way ANOVA (Model x L1)
anova_model = ols('Overall_Score ~ C(Model) + C(L1) + C(Model):C(L1)', data=df).fit()
anova_table = sm.stats.anova_lm(anova_model, typ=2)
anova_table.to_excel(writer, sheet_name='13_TwoWay_ANOVA')

# 5. Correlations & Human Agreement
corr_p = df[['Overall_Score', 'FQI', 'Human_Score', 'Accuracy', 'Helpfulness', 'Specificity']].corr(method='pearson')
corr_p.to_excel(writer, sheet_name='16_Correlations_Pearson')

# 6. OLS Regression
ols_reg = ols('Overall_Score ~ C(Model) + C(Prompt) + C(L1) + C(CEFR) + Error_Density + Lexical_Sophistication', data=df).fit()
with open("analysis_outputs/OLS_Overall_Score_summary.txt", "w") as f:
    f.write(ols_reg.summary().as_text())

writer.close()
print("Statistical Analysis Completed successfully!")

# Generate Figures
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='L1', y='Overall_Score', hue='Prompt', palette='Set2')
plt.title('Feedback Overall Score across L1 Backgrounds and Prompt Types')
plt.tight_layout()
plt.savefig('analysis_outputs/figures/fig2_fairness_L1.png', dpi=300)
plt.close()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_p, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Feedback Metrics')
plt.tight_layout()
plt.savefig('analysis_outputs/figures/fig3_corr_heatmap.png', dpi=300)
plt.close()

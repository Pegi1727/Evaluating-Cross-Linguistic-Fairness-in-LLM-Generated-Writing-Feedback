import os
import json

os.makedirs("notebooks", exist_ok=True)

# 1. Benchmark Notebook Structure
nb1_content = {
 "cells": [
  {"cell_type": "markdown", "metadata": {}, "source": ["# Multilingual LLM Feedback Fairness: Statistical Benchmark\n", "This notebook executes descriptive statistics, ANOVA, non-parametric tests, correlation, and OLS regression."]},
  {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [
   "import pandas as pd\n",
   "import numpy as np\n",
   "import scipy.stats as stats\n",
   "import statsmodels.api as sm\n",
   "from statsmodels.formula.api import ols\n",
   "import matplotlib.pyplot as plt\n",
   "import seaborn as sns\n",
   "\n",
   "df = pd.read_csv('Fairness_Full_Dataset.csv')\n",
   "print('Dataset Shape:', df.shape)\n",
   "df.head()"
  ]},
  {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [
   "# Prompt Effect Test\n",
   "base = df[df['Prompt']=='Baseline']['Overall_Score']\n",
   "fair = df[df['Prompt']=='FairnessAware']['Overall_Score']\n",
   "print('Paired t-test:', stats.ttest_rel(fair, base))\n",
   "print('Wilcoxon test:', stats.wilcoxon(fair, base))"
  ]}
 ],
 "metadata": {"language_info": {"name": "python"}},
 "nbformat": 4,
 "nbformat_minor": 2
}

with open("notebooks/01_Statistical_Analysis_Benchmark.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb1_content, f, indent=2)

# 2. SHAP Notebook Structure
nb2_content = {
 "cells": [
  {"cell_type": "markdown", "metadata": {}, "source": ["# Explainable AI (SHAP) Analysis for LLM Fairness\n", "Interpreting model behavior across non-native learner L1 groups using Tree Explainer."]},
  {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [
   "import pandas as pd\n",
   "import shap\n",
   "from sklearn.ensemble import RandomForestRegressor\n",
   "from sklearn.model_selection import train_test_split\n",
   "\n",
   "df = pd.read_csv('Fairness_Full_Dataset.csv')\n",
   "X = pd.get_dummies(df[['L1', 'CEFR', 'Model', 'Prompt', 'Error_Density', 'Lexical_Sophistication']], drop_first=True)\n",
   "y = df['Overall_Score']\n",
   "\n",
   "model = RandomForestRegressor(n_estimators=100, random_state=42)\n",
   "model.fit(X, y)\n",
   "\n",
   "explainer = shap.TreeExplainer(model)\n",
   "shap_values = explainer.shap_values(X)\n",
   "shap.summary_plot(shap_values, X)"
  ]}
 ],
 "metadata": {"language_info": {"name": "python"}},
 "nbformat": 4,
 "nbformat_minor": 2
}

with open("notebooks/02_Explainable_AI_SHAP_Analysis.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb2_content, f, indent=2)

print("Notebooks successfully generated in notebooks/ directory!")

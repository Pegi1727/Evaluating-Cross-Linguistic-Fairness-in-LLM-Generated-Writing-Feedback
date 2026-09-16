import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import shap

# Load Data
df = pd.read_csv('Fairness_Full_Dataset.csv')

# Preprocessing & One-Hot Encoding
features = ['L1', 'CEFR', 'Model', 'Prompt', 'Error_Density', 'Lexical_Sophistication']
X = pd.get_dummies(df[features], drop_first=True)
y = df['Overall_Score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit Random Forest Surrogate Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print(f"Random Forest R^2 Score: {r2_score(y_test, y_pred):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")

# Compute SHAP Values
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# Plot 1: Feature Importance Summary
plt.figure(figsize=(10, 6))
shap.summary_plot(shap_values, X_test, plot_type="bar", show=False)
plt.title("SHAP Feature Importance for Feedback Overall Score")
plt.tight_layout()
plt.savefig("analysis_outputs/figures/shap_feature_importance.png", dpi=300)
plt.close()

# Plot 2: Beeswarm Plot
plt.figure(figsize=(10, 6))
shap.summary_plot(shap_values, X_test, show=False)
plt.title("SHAP Beeswarm Plot: Impact of L1, Model, and Text Factors")
plt.tight_layout()
plt.savefig("analysis_outputs/figures/shap_beeswarm.png", dpi=300)
plt.close()

print("SHAP Analysis complete. Figures saved.")

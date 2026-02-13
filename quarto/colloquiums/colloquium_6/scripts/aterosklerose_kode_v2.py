# Aterosklerose kode
# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Variables for column names
patient_ID = "Patient ID"
age = "Age"
weight = "Weight (kg)"
hdl = "HDL (mM)"
ldl = "LDL (mM)"
total_cholesterol = "Total Cholesterol (mM)"
risk_random = "Increased risk of Heart Disease?"

# Seed for reproducibility
np.random.seed(42)

# Sample size
n_samples = 100


# Generating random data
data = {
    patient_ID: np.arange(1, n_samples + 1),
    age: np.random.randint(20, 80, n_samples),
    weight: np.random.uniform(50, 120, n_samples).round(1),
    hdl: np.random.uniform(0.2, 3, n_samples).round(1),
    ldl: np.random.uniform(1.5, 4.5, n_samples).round(1),
    total_cholesterol: np.random.uniform(3, 8, n_samples).round(1),
    risk_random: np.random.choice(['Yes', 'No'], n_samples, p=[0.2, 0.8])
}

# Creating DataFrame
patient_data = pd.DataFrame(data)

# Create a figure with subplots
fig, axes = plt.subplots(3, 2, figsize=(14, 18))  # Adjust the grid size based on the number of parameters
axes = axes.flatten()  # Flatten the axis array for easier iteration

# List of parameters to plot
parameters = [age, weight, hdl, ldl, total_cholesterol]

# Loop through the parameters and create a box plot for each
for i, param in enumerate(parameters):
    sns.boxplot(ax=axes[i], data=patient_data, x=risk_random, y=param, palette="Set3", hue = risk_random, legend = False)
    axes[i].set_title(f'{param} Distribution by Heart Disease Risk')
    axes[i].set_xlabel(risk_random)
    axes[i].set_ylabel(param)

# Adjust the layout to prevent overlapping
plt.tight_layout()

# If there's an extra subplot (odd number of parameters), you can remove it
if len(parameters) % 2 != 0:
    fig.delaxes(axes[-1])

plt.show()

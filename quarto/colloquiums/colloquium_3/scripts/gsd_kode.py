import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate 100 patients
n_patients = 100

# Creatine kinase levels
ck_levels = np.concatenate([
    np.random.normal(loc=800, scale=150, size=50),
    np.random.normal(loc=100, scale=50, size=50)
])

# Exercise tolerance score: 1–10 scale
exercise_tolerance = np.concatenate([
    np.random.normal(loc=3.5, scale=1, size=50),
    np.random.normal(loc=7.5, scale=1, size=50) 
])

# Assemble into DataFrame
df_mcardle = pd.DataFrame({
    "patient_id": [f"P{i+1:03d}" for i in range(n_patients)],
    "group": "unknown",
    "Creatine kinase (U/L)": np.round(ck_levels, 1),
    "Exercise tolerance (1-10)": np.round(exercise_tolerance, 1)
})

df_mcardle = df_mcardle.sample(frac=1, random_state=42).reset_index(drop=True)
df_mcardle
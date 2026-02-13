import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 100

# Generate B12 concentrations: normal range 200–900 pg/mL
normal_b12 = np.random.normal(loc=550, scale=150, size=80).clip(200, 900)

# Add some abnormally high values
high_b12 = np.random.normal(loc=2000, scale=100, size=10)

# Add some missing values
missing_b12 = [np.nan] * 10

# Combine all values and shuffle
all_b12 = np.concatenate([normal_b12, high_b12, missing_b12])
np.random.shuffle(all_b12)

# Create DataFrame
df_b12 = pd.DataFrame({
    "sample_id": [f"S{i+1:03d}" for i in range(n_samples)],
    "B12_concentration_pg_per_mL": np.round(all_b12, 1)
})

df_b12
import pandas as pd

# RNA-seq results comparing patient to healthy controls
df = pd.DataFrame({
    "gene": ["APOB", "LDLR", "LCAT", "SCARB1", "CETP", "ABCA1", "LIPC", "PON1"],
    "log2FC": [0.3, -2.1, -1.6, -0.1, 0.9, -0.4, 0.2, -0.2]
})

# Vis datasættet
print("Genudtryk hos patienten sammenlignet med kontroller:")
display(df)
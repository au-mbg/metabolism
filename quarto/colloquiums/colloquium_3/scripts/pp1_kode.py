import pandas as pd
import numpy as np

# Define background proteins with matched, realistic descriptions
receptors = [(f"RECEPTOR{i+1}", "Membrane receptor involved in signal transduction") for i in range(10)]
kinases = [(f"KINASE{i+1}", "Cytoplasmic kinase involved in phosphorylation") for i in range(10)]
transcription_factors = [(f"TF{i+1}", "Transcription factor regulating gene expression") for i in range(10)]

# Define relevant proteins for PP1 question, with realistic names and descriptions
relevant_proteins = [
    ("Protein Phosphatase 1 (PP1)", "Dephosphorylates metabolic enzymes to regulate glycogen metabolism"),
    ("Glycogen Synthase", "Catalyzes formation of glycogen from glucose; activated by PP1"),
    ("Glycogen Phosphorylase", "Breaks down glycogen; inactivated by PP1"),
    ("Phosphorylase Kinase", "Activates glycogen phosphorylase via phosphorylation; inhibited by PP1")
]

# Combine and shuffle
all_proteins = receptors + kinases + transcription_factors + relevant_proteins
np.random.seed(42)
np.random.shuffle(all_proteins)

# Create final DataFrame
df_proteins = pd.DataFrame(all_proteins, columns=["protein_name", "description"])
df_proteins
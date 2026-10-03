"""
knowledge_base.py

Loads the disease knowledge base and provides helper
functions for retrieving disease information.
"""

import pandas as pd

# ==========================================================
# Load Disease Knowledge Base
# ==========================================================

disease_profiles_with_genes_df = pd.read_csv(
    "disease_knowledge_base.csv"
)

# ==========================================================
# Build Disease Lookup Dictionary
# ==========================================================

disease_lookup = {}

for _, row in disease_profiles_with_genes_df.iterrows():

    # Handle missing genes
    genes = row["genes"]
    if pd.isna(genes):
        genes = "Not Available"

    # Handle missing symptoms
    symptoms = row["symptoms"]
    if pd.isna(symptoms):
        symptoms = "Not Available"

    disease_lookup[row["disease_name"]] = {
        "genes": str(genes),
        "symptoms": str(symptoms)
    }

# ==========================================================
# Retrieve Disease Context
# ==========================================================

def get_disease_context(disease_name):

    if disease_name not in disease_lookup:
        return None

    info = disease_lookup[disease_name]

    context = f"""
Disease:
{disease_name}

Associated Symptoms:
{info["symptoms"]}

Associated Genes:
{info["genes"]}
"""

    return context


# ==========================================================
# Retrieve Disease Information
# ==========================================================

def get_disease_info(disease_name):

    if disease_name not in disease_lookup:
        return None

    return disease_lookup[disease_name]
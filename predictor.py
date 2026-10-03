"""
predictor.py

Performs disease retrieval using MiniLM and reranking
using Bio_ClinicalBERT.
"""

import numpy as np
import pandas as pd

from sentence_transformers import SentenceTransformer

from transformers import (
    AutoTokenizer,
    AutoModel
)

import torch

from sklearn.metrics.pairwise import cosine_similarity
from knowledge_base import disease_profiles_with_genes_df



# ----------------------------------------------------
# Load Retrieval Embeddings
# ----------------------------------------------------

retrieval_embeddings = np.load(
    "retrieval_embeddings_v2.npy"
)

# ----------------------------------------------------
# Load Clinical Embeddings
# ----------------------------------------------------

clinical_embeddings = np.load(
    "clinical_embeddings.npy"
)

# ==========================================================
# Synchronize all datasets to the common size
# ==========================================================

common_size = min(
    len(disease_profiles_with_genes_df),
    len(retrieval_embeddings),
    len(clinical_embeddings)
)

print(f"Using common dataset size: {common_size}")

disease_profiles_with_genes_df = (
    disease_profiles_with_genes_df
    .iloc[:common_size]
    .reset_index(drop=True)
)

retrieval_embeddings = retrieval_embeddings[:common_size]
clinical_embeddings = clinical_embeddings[:common_size]

# ----------------------------------------------------
# Load MiniLM Retrieval Model
# ----------------------------------------------------

retrieval_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# ----------------------------------------------------
# Load BioClinicalBERT
# ----------------------------------------------------

tokenizer = AutoTokenizer.from_pretrained(
    "emilyalsentzer/Bio_ClinicalBERT"
)

clinical_model = AutoModel.from_pretrained(
    "emilyalsentzer/Bio_ClinicalBERT"
)

clinical_model.eval()

print("Predictor initialized successfully.")

# ----------------------------------------------------
# Generate ClinicalBERT Embedding
# ----------------------------------------------------

def generate_clinical_embedding(text):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():

        outputs = clinical_model(**inputs)

    embedding = (
        outputs.last_hidden_state
        .mean(dim=1)
        .squeeze()
        .numpy()
    )

    return embedding

# ===========================================================
# Retrieve and Rerank Candidate Diseases
#
# This function performs two-stage disease retrieval:
#
# 1. MiniLM retrieves the Top-50 candidate diseases.
# 2. ClinicalBERT reranks these candidates using the
#    enriched disease profiles.
#
# The reranked diseases are returned in descending order
# of clinical similarity.
# ===========================================================

def retrieve_diseases_final(query):

    # Encode the user's query using MiniLM
    query_embedding = retrieval_model.encode([query])

    similarities = cosine_similarity(
        query_embedding,
        retrieval_embeddings
    )[0]

    best_score = similarities.max()

    if best_score < 0.40:
        return []

    top_indices = similarities.argsort()[-100:][::-1]

    query_embedding = generate_clinical_embedding(query)

    reranked_results = []

    # Rerank candidates using ClinicalBERT
    for idx in top_indices:

        disease_embedding = clinical_embeddings[idx]

        clinical_score = cosine_similarity(
            [query_embedding],
            [disease_embedding]
        )[0][0]

        reranked_results.append(
            (
                disease_profiles_with_genes_df.iloc[idx]["disease_name"],
                float(clinical_score)
            )
        )

    # Sort by ClinicalBERT score
    reranked_results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return reranked_results

print("Disease dataframe:", len(disease_profiles_with_genes_df))
print("Retrieval embeddings:", len(retrieval_embeddings))
print("Clinical embeddings:", len(clinical_embeddings))
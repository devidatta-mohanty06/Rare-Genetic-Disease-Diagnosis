# AI-Powered Rare Genetic Disease Differential Diagnosis Assistant

An AI-powered clinical decision support application designed to assist in the differential diagnosis of rare genetic diseases using Human Phenotype Ontology (HPO), semantic retrieval, biomedical language modeling, a disease–gene knowledge base, and Retrieval-Augmented Generation (RAG).

> **Disclaimer:** This application is intended for research and educational purposes only. It is not a substitute for professional medical diagnosis, clinical judgment, or genetic counselling.

---

## Project Overview

Rare genetic diseases are often difficult to diagnose because many disorders share overlapping clinical manifestations. This project develops an AI-assisted differential diagnosis system that takes patient symptoms as input and retrieves and ranks potentially relevant rare genetic diseases.

The system combines:

- Human Phenotype Ontology (HPO) based phenotype information
- MiniLM semantic retrieval
- BioClinicalBERT contextual re-ranking
- Disease–gene knowledge base
- Gemini-based Retrieval-Augmented Generation (RAG)
- Streamlit web application

The system produces a ranked list of candidate diseases and generates a knowledge-grounded AI-assisted clinical interpretation.

---

## System Workflow

```text
Patient Symptoms
       ↓
MiniLM Semantic Retrieval
       ↓
Top-100 Candidate Diseases
       ↓
BioClinicalBERT Re-ranking
       ↓
Top-5 Candidate Diseases
       ↓
Disease–Gene Knowledge Base
       ↓
Gemini RAG
       ↓
AI-Assisted Clinical Interpretation
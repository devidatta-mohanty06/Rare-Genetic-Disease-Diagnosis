from google import genai

from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_clinical_summary(
    patient_symptoms,
    disease_name,
    genes,
    disease_symptoms,
):

    prompt = f"""
You are an expert clinical decision support assistant.

The diagnosis has already been predicted using an AI pipeline consisting of Human Phenotype Ontology (HPO), MiniLM retrieval, and BioClinicalBERT reranking.

Use ONLY the information provided below.

Patient Symptoms:
{patient_symptoms}

Predicted Disease:
{disease_name}

Associated Genes:
{genes}

Known Disease Symptoms:
{disease_symptoms}

Generate a well-structured clinical report using Markdown.

# Disease Overview
Briefly describe the disease in 3-4 sentences.

# Why this Disease Matches
Explain only using the supplied patient symptoms.
Do NOT assume symptoms that are not provided.

# Associated Gene(s)
Briefly explain the role of the associated gene(s).

# Recommended Diagnostic Tests
Provide only 4–6 important tests as bullet points.

# Treatment Options
Provide concise bullet points.

# Prognosis
Maximum 3 sentences.

# Specialist Referral
Provide bullet points only.

# Disclaimer
State that this report is AI-assisted, intended for educational purposes, and that clinical evaluation and genetic testing are required before confirming a diagnosis.

Rules:
- Keep the report concise.
- Avoid repeating information.
- Use bullet points wherever appropriate.
- Do not hallucinate symptoms or findings.
- Use professional medical language.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:

        return f"""
❌ Gemini Error

{type(e).__name__}

{str(e)}
"""
import streamlit as st


def show_methodology():

    st.title("📖 System Methodology")

    st.markdown("""
This application implements an **AI-assisted clinical decision support pipeline**
for the differential diagnosis of **rare genetic diseases** by integrating
semantic retrieval, transformer-based reranking, a disease–gene knowledge base,
and Retrieval-Augmented Generation (RAG).
""")

    st.divider()

    # ---------------- System Workflow ---------------- #

    st.subheader("🔬 System Workflow")

    st.info("""
🩺 **Patient Symptoms**

⬇️

🔍 **MiniLM Semantic Retrieval**

⬇️

📋 **Top-100 Candidate Diseases**

⬇️

🧠 **BioClinicalBERT Re-ranking**

⬇️

🏆 **Top-5 Predicted Diseases**

⬇️

🧬 **Disease–Gene Knowledge Base**

⬇️

🤖 **Gemini AI (Retrieval-Augmented Generation)**

⬇️

📄 **AI-Assisted Clinical Interpretation**
""")

    st.divider()

    # ---------------- Pipeline ---------------- #

    st.subheader("⚙️ AI Pipeline")

    with st.expander("Step 1 — Patient Symptom Input", expanded=True):
        st.write("""
The clinician enters the patient's observed symptoms in natural language.
Examples include hearing loss, developmental delay, muscle weakness,
seizures, or vision impairment.
""")

    with st.expander("Step 2 — Semantic Retrieval"):
        st.write("""
MiniLM converts the symptom description into a dense embedding and retrieves
the most semantically similar disease profiles from the Human Phenotype
Ontology dataset.
""")

    with st.expander("Step 3 — BioClinicalBERT Re-ranking"):
        st.write("""
The retrieved diseases are re-ranked using BioClinicalBERT, a transformer model
trained on biomedical and clinical literature, to improve the relevance of
predicted diseases.
""")

    with st.expander("Step 4 — Disease–Gene Knowledge Base"):
        st.write("""
Associated genes and phenotype information are retrieved for the highest-ranked
diseases to provide biological context and improve interpretability.
""")

    with st.expander("Step 5 — AI Clinical Interpretation"):
        st.write("""
Gemini AI uses Retrieval-Augmented Generation (RAG) to generate a concise,
structured clinical interpretation based solely on the retrieved disease
information and patient symptoms.
""")

    st.divider()

    # ---------------- Technologies ---------------- #

    st.subheader("🛠 Technologies Used")

    col1, col2 = st.columns(2)

    with col1:
        st.success("""
**Frontend**
- Streamlit

**Programming Language**
- Python

**Data Processing**
- Pandas
- NumPy
""")

    with col2:
        st.success("""
**AI Models**
- MiniLM
- BioClinicalBERT
- Gemini 2.5 Flash

**Knowledge Source**
- Human Phenotype Ontology (HPO)
""")

    st.divider()

    # ---------------- Features ---------------- #

    st.subheader("🚀 Key Features")

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
✅ Semantic symptom matching

✅ Differential diagnosis

✅ Disease–gene association

✅ Top-5 disease prediction
""")

    with col2:
        st.info("""
✅ Retrieval-Augmented Generation

✅ AI clinical interpretation

✅ Explainable AI workflow

✅ Interactive web application
""")

    st.divider()

    # ---------------- Limitations ---------------- #

    st.subheader("⚠️ Limitations")

    st.warning("""
• Intended for educational and research purposes only.

• Diagnostic quality depends on the completeness of phenotype annotations.

• Does not replace clinical evaluation or genetic testing.

• AI-generated reports should always be reviewed by qualified healthcare professionals.
""")
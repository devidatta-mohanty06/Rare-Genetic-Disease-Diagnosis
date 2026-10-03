import streamlit as st


def show_about():

    st.title("ℹ️ About")

    st.markdown("""
## 🧬 AI-Powered Differential Diagnosis Assistant

This application is an **AI-assisted Clinical Decision Support System (CDSS)**
developed to support the differential diagnosis of **rare genetic diseases**
using patient phenotype information.

The system combines semantic retrieval, transformer-based reranking,
disease–gene knowledge integration, and Retrieval-Augmented Generation (RAG)
to provide clinically relevant disease predictions along with an AI-assisted
clinical interpretation.
""")

    st.divider()

    # ---------------- Objective ---------------- #

    st.subheader("🎯 Project Objective")

    st.info("""
The objective of this project is to assist healthcare professionals and
researchers by providing an intelligent system capable of:

• Predicting rare genetic diseases from patient symptoms.

• Identifying disease-associated genes.

• Generating AI-assisted clinical interpretations.

• Supporting clinical decision-making through explainable AI.
""")

    st.divider()

    # ---------------- Core Technologies ---------------- #

    st.subheader("🛠 Core Technologies")

    col1, col2 = st.columns(2)

    with col1:
        st.success("""
**Artificial Intelligence**

• MiniLM Semantic Retrieval

• BioClinicalBERT

• Google Gemini 2.5 Flash

• Retrieval-Augmented Generation (RAG)
""")

    with col2:
        st.success("""
**Development Stack**

• Python

• Streamlit

• Pandas

• NumPy

• Human Phenotype Ontology (HPO)
""")

    st.divider()

    # ---------------- Key Features ---------------- #

    st.subheader("🚀 Key Features")

    st.markdown("""
- 🧬 Rare genetic disease prediction

- 🧠 Semantic symptom matching

- 🔍 BioClinicalBERT reranking

- 🧬 Disease–gene association

- 🤖 AI-assisted clinical interpretation

- 📄 Explainable AI workflow

- 🌐 Interactive Streamlit interface
""")

    st.divider()

    # ---------------- Developer ---------------- #

    st.subheader("👨‍💻 Developed By")

    st.markdown("""
**Devidatta Mohanty**

M.Sc. Bioinformatics

Amity University, Noida

Academic Project (2026)
""")

    st.divider()

    # ---------------- Future Scope ---------------- #

    st.subheader("🔮 Future Scope")

    st.info("""
Future enhancements may include:

• Integration with Electronic Health Records (EHR)

• Incorporation of genomic sequencing data

• Drug recommendation support

• Multi-modal diagnosis using medical imaging

• Explainable AI visualizations

• Clinical validation using real-world patient data
""")

    st.divider()

    # ---------------- Disclaimer ---------------- #

    st.warning("""
### Disclaimer

This application has been developed solely for **educational and research purposes**.

It is intended to assist clinical interpretation and should **not** be considered
a substitute for professional medical diagnosis, clinical evaluation,
or genetic testing.
""")
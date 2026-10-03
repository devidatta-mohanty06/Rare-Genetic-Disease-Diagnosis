import streamlit as st


def show_dashboard():

    # ---------------- Hero Section ---------------- #

    st.markdown(
    """
    <div class="card">

    <h1 class="main-title">
    🧬 AI-Powered Differential Diagnosis Assistant
    </h1>

    <p class="subtitle">
    Clinical Decision Support System for Rare Genetic Diseases
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.write("")

    # ---------------- Statistics ---------------- #

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">12,567</div>
            <div class="metric-title">Disease Profiles</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">185,315</div>
            <div class="metric-title">Associated Genes</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">19,000+</div>
            <div class="metric-title">HPO Terms</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">RAG-Based</div>
            <div class="metric-title">Architecture</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ---------------- Project Overview ---------------- #

    st.subheader("📖 Project Overview")

    st.markdown("""
This application is an **AI-assisted clinical decision support system** developed to aid the differential diagnosis of **rare genetic diseases**.

The system combines **Human Phenotype Ontology (HPO)**, **MiniLM semantic retrieval**, **BioClinicalBERT reranking**, and **Retrieval-Augmented Generation (Gemini AI)** to identify clinically relevant diseases based on patient symptoms and generate an AI-assisted clinical interpretation.
""")

    st.divider()

    # ---------------- Workflow ---------------- #

    st.subheader("🔬 AI Workflow")

    st.info("""
🩺 Patient Symptoms

⬇️

🔍 MiniLM Semantic Retrieval

⬇️

🧠 BioClinicalBERT Re-ranking

⬇️

🧬 Disease–Gene Knowledge Base

⬇️

🤖 Gemini AI (Retrieval-Augmented Generation)

⬇️

📄 AI-Assisted Clinical Interpretation
""")

    st.divider()

    # ---------------- Features ---------------- #

    st.subheader("🚀 Key Features")

    col1, col2 = st.columns(2)

    with col1:
        st.success("""
✓ Differential Diagnosis

✓ Semantic Symptom Matching

✓ Gene Association

✓ Top-5 Disease Prediction
""")

    with col2:
        st.success("""
✓ AI Clinical Interpretation

✓ Retrieval-Augmented Generation

✓ Explainable AI Pipeline

✓ Interactive Streamlit Interface
""")

    st.divider()

    # ---------------- Technologies ---------------- #

    st.subheader("⚙️ Technologies Used")

    st.markdown("""
- 🐍 Python
- 🎈 Streamlit
- 🤗 Sentence Transformers (MiniLM)
- 🧠 BioClinicalBERT
- 🧬 Human Phenotype Ontology (HPO)
- 📊 NumPy & Pandas
- 🤖 Google Gemini AI
""")

    st.divider()

    # ---------------- Disclaimer ---------------- #

    st.warning("""
**Disclaimer**

This application is intended solely for **educational and research purposes**.

It is designed to assist with clinical interpretation and should **not** be used as a substitute for professional medical diagnosis, clinical evaluation, or genetic testing.
""")
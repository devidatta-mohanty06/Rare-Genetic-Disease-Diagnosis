import streamlit as st

from predictor import retrieve_diseases_final
from knowledge_base import get_disease_info
from rag import generate_clinical_summary


# ---------------- SESSION STATE ---------------- #

if "results" not in st.session_state:
    st.session_state.results = None

if "symptoms" not in st.session_state:
    st.session_state.symptoms = ""

# ------------------------------------------------ #


def show_diagnosis():

    st.title("🔍 Disease Diagnosis")

    st.markdown("""
Enter the patient's symptoms below.

**Example Symptoms**
- Hearing loss
- Speech delay
- Delayed language development
- Muscle weakness
- Seizures
""")

    symptoms = st.text_area(
        "Patient Symptoms",
        height=180,
        placeholder="Type symptoms separated by commas..."
    )

    # ---------------- Predict Disease ---------------- #

    if st.button("🧬 Predict Disease", use_container_width=True):

        if not symptoms.strip():
            st.warning("Please enter patient symptoms.")
            return

        with st.spinner("Analyzing symptoms..."):
            results = retrieve_diseases_final(symptoms)

        st.session_state.results = results
        st.session_state.symptoms = symptoms

    # ---------------- Display Results ---------------- #

    if st.session_state.results is not None:

        results = st.session_state.results
        symptoms = st.session_state.symptoms

        if len(results) == 0:
            st.error("No matching diseases found.")
            return

        st.success("Analysis Complete")

        st.markdown("---")
        st.subheader("🧬 Top Predicted Diseases")

        top_disease = None
        top_info = None

        for rank, (disease, score) in enumerate(results[:5], start=1):

            score = float(score)
            info = get_disease_info(disease)

            if rank == 1:
                top_disease = disease
                top_info = info

            with st.container():

                st.markdown(f"## 🧬 {rank}. {disease}")

                st.metric(
                    "Clinical Similarity Score",
                    f"{score:.3f}"
                )

                if info:

                    # ---------------- Genes ---------------- #

                    st.markdown("### 🧬 Associated Gene(s)")

                    genes = str(info.get("genes", "Not Available"))

                    if genes == "Not Available" or genes.strip() == "":
                        st.info("No associated genes available.")
                    else:
                        for gene in genes.split(","):
                            gene = gene.strip()
                            if gene:
                                st.markdown(f"- **{gene}**")

                    # ---------------- Symptoms ---------------- #

                    st.markdown("### 🩺 Associated Symptoms")

                    symptoms_data = str(info.get("symptoms", "Not Available"))

                    if symptoms_data == "Not Available" or symptoms_data.strip() == "":
                        st.info("No associated symptoms available.")
                    else:

                        delimiter = ";" if ";" in symptoms_data else ","

                        for symptom in symptoms_data.split(delimiter):

                            symptom = symptom.strip()

                            if symptom:
                                st.markdown(f"- {symptom}")

                st.markdown("---")

        # ---------------- AI Clinical Interpretation ---------------- #

        if top_disease and top_info:

            st.subheader("🧠 AI-Assisted Clinical Interpretation")

            st.info(
                f"""
**Predicted Disease:** **{top_disease}**

The following report is generated using the highest-ranked disease predicted by the retrieval pipeline (MiniLM + BioClinicalBERT).

This report is intended for educational and research purposes and should support—not replace—clinical judgment.
"""
            )

            if st.button(
                "📄 Generate AI Clinical Report",
                key="generate_report",
                use_container_width=True
            ):

                with st.spinner("Generating AI Clinical Report..."):

                    summary = generate_clinical_summary(
                        patient_symptoms=symptoms,
                        disease_name=top_disease,
                        genes=top_info["genes"],
                        disease_symptoms=top_info["symptoms"]
                    )

                st.markdown("---")
                st.markdown("# 📄 AI Clinical Report")

                st.markdown(summary)

                st.warning(
                    """
**Disclaimer**

This AI-generated report is intended for educational and research purposes only.

It should **not** be considered a definitive medical diagnosis.

Clinical evaluation, laboratory investigations, and genetic testing are recommended before any medical decision is made.
"""
                )
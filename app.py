import streamlit as st
from streamlit_option_menu import option_menu

# Import Components
from components.dashboard import show_dashboard
from components.diagnosis import show_diagnosis
from components.methodology import show_methodology
from components.about import show_about


# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="AI-Powered Differential Diagnosis Assistant",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# LOAD CSS
# ----------------------------------------------------

def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#load_css()

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <h2 style='text-align:center;color:#2563EB;'>
        🧬 Rare Disease AI
        </h2>
        """,
        unsafe_allow_html=True
    )

    selected = option_menu(
        menu_title=None,

        options=[
            "Dashboard",
            "Diagnosis",
            "Methodology",
            "About"
        ],

        icons=[
            "house-fill",
            "search",
            "journal-medical",
            "info-circle"
        ],

        default_index=0,

        styles={
            "container": {
                "padding": "5!important",
                "background-color": "#ffffff"
            },

            "icon": {
                "color": "#2563EB",
                "font-size": "18px"
            },

            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px",
                "color": "#1F2937",
                "--hover-color": "#EAF3FF"
            },

            "nav-link-selected": {
                "background-color": "#2563EB",
                "color": "white",
            },
        }
    )

    st.markdown("---")

    st.markdown(
        """
        ### Developed By

        **Devidatta Mohanty**

        M.Sc. Bioinformatics

        Amity University
        """
    )

# ----------------------------------------------------
# ROUTING
# ----------------------------------------------------

if selected == "Dashboard":
    show_dashboard()

elif selected == "Diagnosis":
    show_diagnosis()

elif selected == "Methodology":
    show_methodology()

elif selected == "About":
    show_about()
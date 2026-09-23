import streamlit as st

from data.profile import PROJECT_LINKS

st.title("HealthLensAI")
st.subheader("AI-powered medical report analysis with LangGraph-orchestrated agents")

st.markdown(
    "I built **HealthLensAI** using **LangGraph** to orchestrate AI agents, "
    "with a **Streamlit** interface for reviewing medical report insights. "
    "The application analyzes medical report data, identifies health trends, "
    "and helps surface possible risk indicators for deeper review."
)

st.link_button(
    "Open the live HealthLensAI app",
    PROJECT_LINKS["HealthLensAI"],
    icon=":material/open_in_new:",
    type="primary",
    width="content",
)

st.markdown("### Project focus")
left, middle, right = st.columns(3)
with left:
    st.markdown("#### Report analysis")
    st.write("Reads medical report information and turns it into concise, review-ready insights.")
with middle:
    st.markdown("#### Trend insights")
    st.write("Highlights patterns across health metrics so changes are easier to understand.")
with right:
    st.markdown("#### Risk review")
    st.write("Surfaces possible health risk indicators through an agent-driven workflow.")

st.markdown("### Technologies")
st.markdown("LangGraph · AI agents · Python · Streamlit")

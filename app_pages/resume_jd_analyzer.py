import streamlit as st

st.title("Resume–Job Description Analyzer")
st.subheader("A RAG-based system for actionable skill-gap analysis")

st.markdown(
    """
I’ve built the latest version of a **RAG-based system** that analyzes the skill gap
between a resume and a job description. It identifies **matching skills, missing
skills, and areas that may need improvement**, helping candidates make their
experience more relevant to the role they are targeting.
"""
)

st.link_button(
    "Open the live Resume–JD Analyzer",
    "https://resumejd-analyzer.streamlit.app/",
    width="content",
)

st.markdown("### What it provides")
left, middle, right = st.columns(3)
with left:
    st.markdown("#### Matching skills")
    st.write("Highlights the capabilities and experience shared by the resume and job description.")
with middle:
    st.markdown("#### Missing skills")
    st.write("Surfaces important requirements present in the role but not clearly represented in the resume.")
with right:
    st.markdown("#### Improvement areas")
    st.write("Provides practical direction for strengthening the resume and closing relevant skill gaps.")

st.markdown("### Project focus")
st.markdown(
    "RAG · Resume intelligence · Job-description analysis · Skill extraction · "
    "Gap analysis · GenAI"
)

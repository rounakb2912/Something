import streamlit as st
import pandas as pd
import random
import os
from datetime import datetime, date

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="My Digital Profile",
    page_icon="🚀",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
    color: white;
}

.main {
    padding: 2rem 5rem;
}

.hero {
    text-align: center;
    padding: 80px 20px 50px 20px;
}

.hero h1 {
    font-size: 55px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 20px;
    color: #94a3b8;
}

.section {
    padding: 35px 0;
}

.card {
    background-color: #1e293b;
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 20px;
}

.card h3 {
    margin-top: 0;
}

a {
    text-decoration: none;
}

</style>
""", unsafe_allow_html=True)


# ---------- HERO ----------
st.markdown("""
<div class="hero">

<h1>Hey, I'm Rounak 👋</h1>

<p>
Developer • AI/ML Enthusiast • Builder
</p>

<p>
I'm learning, building projects and connecting with
people who can help me grow.
</p>

</div>
""", unsafe_allow_html=True)


# ---------- SOCIAL LINKS ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/rounak-bhatiya/")

with col2:
    st.link_button("GitHub", "https://github.com/rounakb2912")

with col3:
    st.link_button("Email Me", "mailto:bhatiarounak467@gmail.com")


# ---------- ABOUT ----------
st.markdown('<div class="section">', unsafe_allow_html=True)

st.header("About Me")

st.write("""
I'm currently learning software development, Python, SQL and AI/ML.

I enjoy building things, experimenting with technology and learning
from people who are more experienced than me.
""")

st.markdown('</div>', unsafe_allow_html=True)


# ---------- SKILLS ----------
st.header("Skills")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### 🐍 Python")
    
with col2:
    st.markdown("### 🗄️ SQL")

with col3:
    st.markdown("### 🤖 AI / ML")

with col4:
    st.markdown("### 🌐 Web")


# ---------- PROJECTS ----------
st.header("Projects")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h3>🚀 Project One</h3>
    <p>
    Short description of your project.
    Explain what you built and what technology you used.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button("View Project", "https://coursera.org/share/f619f52046223762feaa7f8b21630799")



# ---------- CURRENTLY LEARNING ----------
st.header("Currently Learning")

st.write("""
- Python
- SQL
- AI / Machine Learning
- Streamlit
- Git & GitHub
""")


# ---------- ACHIEVEMENTS ----------
st.header("Achievements & Certificates")

st.markdown("""
<div class="card">

🏆 Certificate / Achievement 1

    st.link_button("View Certificate","https://coursera.org/share/f619f52046223762feaa7f8b21630799"
</div>
""", unsafe_allow_html=True)


# ---------- CONNECT ----------
st.header("Let's Connect 🤝")

st.write(
    "I'm always interested in meeting developers, seniors,"
    "fellow learners"
    "mentors and people working in technology."
)

st.link_button(
    "Connect with me on LinkedIn",
    "https://www.linkedin.com/in/rounak-bhatiya/"
)


# ---------- FOOTER ----------
st.markdown("---")

st.caption("Built with Python + Streamlit 🚀")

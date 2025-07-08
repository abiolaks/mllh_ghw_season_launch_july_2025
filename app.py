import streamlit as st

# Set page config
st.set_page_config(page_title="My Portfolio", layout="wide")

# Read static files
with open("web_dev/index.html", "r", encoding="utf-8") as f:
    html = f.read()
with open("web_dev/style.css", "r", encoding="utf-8") as f:
    css = f.read()
with open("web_dev/script.js", "r", encoding="utf-8") as f:
    js = f.read()

# Inject CSS
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Display HTML
st.components.v1.html(
    html + f"<script>{js}</script>",
    height=1200,
    scrolling=True
)

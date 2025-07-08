import streamlit as st
import base64
import re


# Helper to encode image to base64
def img_to_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# Read static files
with open("web_dev/index.html", "r", encoding="utf-8") as f:
    html = f.read()
with open("web_dev/style.css", "r", encoding="utf-8") as f:
    css = f.read()
with open("web_dev/script.js", "r", encoding="utf-8") as f:
    js = f.read()

# Inline CSS and JS
html = re.sub(
    r'<link rel="stylesheet" href="style.css">', f"<style>{css}</style>", html
)
html = re.sub(r'<script src="script.js"></script>', f"<script>{js}</script>", html)

# Replace image src with base64
img_map = {
    "profile.jpg": img_to_base64("web_dev/images/profile.jpg"),
    "project1.png": img_to_base64("web_dev/images/project1.png"),
    "project2.png": img_to_base64("web_dev/images/project2.png"),
    "project3.png": img_to_base64("web_dev/images/project3.png"),
}
for name, b64 in img_map.items():
    html = html.replace(
        f"images/{name}", f"data:image/{name.split('.')[-1]};base64,{b64}"
    )

# Streamlit config
st.set_page_config(page_title="My Portfolio", layout="wide")

# Render HTML
st.components.v1.html(html, height=1400, scrolling=True)

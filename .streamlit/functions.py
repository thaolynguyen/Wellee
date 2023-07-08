import streamlit as st
from PIL import Image

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url(https://webgradients.com/public/webgradients_png/014%20Amy%20Crisp.png)
             background-attachment: fixed;
             background-size: cover
             opacity : 0.5
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
#             background-image: url("https://img.freepik.com/free-vector/watercolor-chinese-style-illustration_23-2149727906.jpg?w=740&t=st=1688745096~exp=1688745696~hmac=a5741e891bad25bef7084d1020ef92bf30394cab8cde826852d554ac6b2251be");


def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo
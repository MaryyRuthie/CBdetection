import streamlit as st
from PIL import Image

hide_menu = """
<style>
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}
</style>
"""

showWarningOnDirectExecution = False
image = Image.open('icons/logo.png')


st.set_page_config(page_title = "L", page_icon = image)

st.markdown(hide_menu, unsafe_allow_html=True)

 
st.sidebar.image(image , use_column_width=True, output_format='auto')


st.sidebar.markdown("---")


st.sidebar.markdown("<br> <br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>© 2023 | Pravin Bante</h1>", unsafe_allow_html=True)




st.title("L")
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("Hey I'am Mariya Rajan")  
st.markdown(" <br> ", unsafe_allow_html=True)
st.markdown("   Project  **_CyberGuard_** developed . It focuses on :blue[**_Cyber Bullying Detection Application is a Machine Learning Web application for Cyber Bullying Detection_**].")
st.markdown(" <br> ", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(" contact <a href=mailto:mariyarajan77@gmail.com>Mariya Rajan</a> .", unsafe_allow_html=True)
st.markdown("<br> <br> <br>", unsafe_allow_html=True)
col1, col2 = st.columns([2,4])
with col1:
    image = Image.open('icons/nfsulogo.png')
    st.image(image, use_column_width=False, output_format='auto')
with col2:
    st.markdown("<br> ", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 15px; color: #002d51;'>National Forensic Science University Ghandhinagar, Gujrata</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 15px; color: #002d51;'>M.tech in Cyber Security & Digital Forensic</h1>", unsafe_allow_html=True)

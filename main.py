import streamlit as st

st.set_page_config(layout="centered")

col1, col2 = st.columns(2)

with col1:
    st.image("images/profile.jpg", width=300)

with col2:
    st.title("Chris Reid")
    content = """
    Hi, I am Chris! I am a Python developer, avid curler and aspiring rock
    guitarist
    """
    st.info(content)

description = """
Below you can find some of the apps I have built in Python. Feel free to 
contact me!
"""
st.write(description)

import streamlit as st
import pandas

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

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

df = pandas.read_csv("data.csv", sep=";")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
import pandas as pd
#from vega_datasets import data
import streamlit as st
import altair as alt
from PIL import Image

def main():
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration"])

    if page == "Homepage":
        image = Image.open('sunrise.png')

        st.image(image)

        st.header("This is your data explorer.")
        st.write("Please select a page on the left.")
    elif page == "Exploration":
        image = Image.open('sunrise.png')

        st.image(image)
        st.title("Data Exploration")


@st.cache


if __name__ == "__main__":
    main()

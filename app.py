import pandas as pd
#from vega_datasets import data
import streamlit as st
import altair as alt
from PIL import Image

def main():
    df = load_data()
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration"])

    if page == "Homepage":
        image = Image.open('sunrise.png')

        st.image(image)

        st.header("This is your data explorer.")
        st.write("Please select a page on the left.")
        st.write(df)
    elif page == "Exploration":
        image = Image.open('sunrise.png')

        st.image(image)
        st.title("Data Exploration")

        x_axis = st.selectbox("Choose a variable for the x-axis", df.columns, index=3)#era 3
        y_axis = st.selectbox("Choose a variable for the y-axis", df.columns, index=4)# era 4
        visualize_data(df, x_axis, y_axis)

@st.cache
def load_data():
    df = pd.read_csv('excel.csv',index_col=0)
#    df = data.cars()
    return df

def visualize_data(df, x_axis, y_axis):
    graph = alt.Chart(df).mark_circle(size=60).encode(
        x=x_axis,
        y=y_axis,
        color='CLASSE',
        tooltip=['index', 'SHARPE', 'ADMIN', 'GESTOR']
    ).interactive()

    st.write(graph)

if __name__ == "__main__":
    main()

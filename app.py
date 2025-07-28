import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Online Data Analyzer")

uploaded_file = st.file_uploader("Upload CSV File", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview", df.head())

    st.write("### Summary Stats")
    st.write(df.describe())

    chart_type = st.selectbox("Select Chart Type", ["Bar", "Line", "Scatter"])
    x_axis = st.selectbox("X Axis", df.columns)
    y_axis = st.selectbox("Y Axis", df.columns)

    if chart_type == "Bar":
        fig = px.bar(df, x=x_axis, y=y_axis)
    elif chart_type == "Line":
        fig = px.line(df, x=x_axis, y=y_axis)
    else:
        fig = px.scatter(df, x=x_axis, y=y_axis)

    st.plotly_chart(fig)

import streamlit as st
import plotly_express as px
import pandas as pd

st.title("Data Visualition by COSMOS")
st.sidebar.subheader(("Settings"))
file = st.sidebar.file_uploader(label="Upload file", type=['csv', 'xlsx'])

if file is not None:
    st.subheader(file.name)
    try:
        df = pd.read_csv(file)
    except Exception as e:
        print(e)
        df = pd.read_excel(file)
    try:
        st.write(df)
    except Exception as e:
        print(e)
        st.write("Please upload a file")
    try:
        num_column = list(df.select_dtypes(['float', 'int']).columns)
    except Exception as e:
        print(e)
    chart_sel = st.sidebar.selectbox(
        label="Select the chart type",
        options=['ScatterPlot', 'LinePlot', 'Histogram', 'BoxPlot', 'BarGraph']
    )

    if chart_sel == 'ScatterPlot':
        st.sidebar.subheader("Scatterplot Settings")
        try:
            x_value = st.sidebar.selectbox('X axis', options=num_column)
            Y_value = st.sidebar.selectbox('Y axis', options=num_column)
            plot = px.scatter(data_frame=df, x=x_value, y=Y_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    elif chart_sel == 'LinePlot':
        st.sidebar.subheader("LinePlot Settings")
        try:
            x_value = st.sidebar.selectbox('X axis', options=num_column)
            Y_value = st.sidebar.selectbox('Y axis', options=num_column)
            plot = px.line(data_frame=df, x=x_value, y=Y_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    elif chart_sel == 'Histogram':
        st.sidebar.subheader("Histogram Settings")
        try:
            x_value = st.sidebar.selectbox('X axis', options=num_column)
            Y_value = st.sidebar.selectbox('Y axis', options=num_column)
            plot = px.histogram(data_frame=df, x=x_value, y=Y_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    elif chart_sel == 'BoxPlot':
        st.sidebar.subheader("BoxPlot Settings")
        try:
            x_value = st.sidebar.selectbox('X axis', options=num_column)
            Y_value = st.sidebar.selectbox('Y axis', options=num_column)
            plot = px.box(data_frame=df, x=x_value, y=Y_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    elif chart_sel == 'BarGraph':
        st.sidebar.subheader("BarGraph Settings")
        try:
            x_value = st.sidebar.selectbox('X axis', options=num_column)
            Y_value = st.sidebar.selectbox('Y axis', options=num_column)
            plot = px.bar(data_frame=df, x=x_value, y=Y_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
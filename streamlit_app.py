import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Interactive dashboard")
data = pd.read_csv("emp.csv")
pxlot = px.bar(data, x='Dept', y='Sal', title='Salary by Department')
st.plotly_chart(pxlot)
features = st.multiselect("Select Features", options=data.columns.tolist(), default=['Dept', 'Sal'])
st.write(data[features])

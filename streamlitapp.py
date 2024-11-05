# Import necessary libraries
import streamlit as st
import seaborn as sns 
import plotly.express as px
import pandas as pd

# --- Title and Introduction ---
st.title("Plotly and Streamlit Interactive Visualizations")

# Author information
st.markdown("<h5 style='color: teal;'>Created by:</h6>", unsafe_allow_html=True)
st.markdown("<p style='color: white;'>1. USN _ FULLNAME </p>", unsafe_allow_html=True)


tips = sns.load_dataset('tips')  # Loading the dataset
print(tips.head())  # This will show the first 5 rows of the tips dataset

# --- Task 2: Bar Chart ---
st.subheader("Task 2: Bar Chart")
#Bar Chart: Average Tip by Day (With Color)
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white',  # Clean white background
)
fig2.show()
st.plotly_chart(fig2)

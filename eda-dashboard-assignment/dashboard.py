# dashboard.py

import streamlit as st
import plotly.express as px
from fetch_data import get_clean_data

# -------------------------------
# Page Title
# -------------------------------
st.title("📊 Simple Data Dashboard")

# -------------------------------
# Load Data
# -------------------------------
df = get_clean_data()

if df.empty:
    st.error("Failed to load data")
    st.stop()

# -------------------------------
# Dataset Preview
# -------------------------------
st.subheader("Dataset Preview")
st.dataframe(df.head())

# -------------------------------
# Posts per User (EDA)
# -------------------------------
posts_per_user = df.groupby("user_id").size().reset_index(name="post_count")

fig1 = px.bar(posts_per_user,
              x="user_id",
              y="post_count",
              title="Posts per User")

st.subheader("Posts per User")
st.plotly_chart(fig1)

# Observation:
# Each user has created equal number of posts

# -------------------------------
# Post Length Distribution
# -------------------------------
fig2 = px.histogram(df,
                    x="post_length",
                    nbins=20,
                    title="Distribution of Post Length")

st.subheader("Post Length Distribution")
st.plotly_chart(fig2)

# Observation:
# Most posts fall within a similar length range

# -------------------------------
# End
# -------------------------------
st.success("Dashboard Loaded Successfully!")
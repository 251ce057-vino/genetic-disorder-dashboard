import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Genetic Disorder Risk Dashboard",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 Genetic Disorder Risk Prioritization")
st.write("AI-based genetic disorder risk prediction dashboard")

# Load prediction results
df = pd.read_csv("patient_priority_results.csv")

# Summary metrics
total = len(df)
high = (df["Priority Level"] == "High").sum()
medium = (df["Priority Level"] == "Medium").sum()
low = (df["Priority Level"] == "Low").sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Records", total)
c2.metric("High Priority", high)
c3.metric("Medium Priority", medium)
c4.metric("Low Priority", low)

st.subheader("Priority Distribution")

counts = df["Priority Level"].value_counts().reindex(
    ["High", "Medium", "Low"], fill_value=0
)

st.bar_chart(counts)

st.subheader("Patient Prediction Results")

search = st.text_input("Search by predicted category")

if search:
    df = df[df["Predicted Category"].str.contains(
        search, case=False, na=False
    )]

st.dataframe(df, use_container_width=True)

st.download_button(
    "Download Results CSV",
    data=df.to_csv(index=False),
    file_name="patient_priority_results.csv",
    mime="text/csv"
)

st.caption(
    "Educational project only. Predictions are not a medical diagnosis."
)

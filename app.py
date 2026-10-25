
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Genetic Disorder Risk Dashboard",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 Genetic Disorder Risk Prioritization")
st.write("AI-Based Genetic Disorder Risk Prediction Dashboard")

# Load results
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

# Priority chart
st.subheader("Priority Distribution")

counts = df["Priority Level"].value_counts().reindex(
    ["High", "Medium", "Low"], fill_value=0
)

fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.bar(counts.index, counts.values)

ax.set_xlabel("Priority Level")
ax.set_ylabel("Number of Records")
ax.set_title("Patient Priority Distribution")
ax.bar_label(bars, fmt="%d")
ax.grid(axis="y", linestyle="--", alpha=0.3)

st.pyplot(fig)
plt.close(fig)

# Search and results
st.subheader("Patient Prediction Results")

search = st.text_input("Search by predicted category")

filtered_df = df.copy()

if search:
    filtered_df = filtered_df[
        filtered_df["Predicted Category"].astype(str).str.contains(
            search, case=False, na=False
        )
    ]

st.dataframe(filtered_df, use_container_width=True)

st.download_button(
    "Download Results CSV",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="patient_priority_results.csv",
    mime="text/csv"
)

st.caption(
    "Educational project only. Predictions are not a medical diagnosis."
)

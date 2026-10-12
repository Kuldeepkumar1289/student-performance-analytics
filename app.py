import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="SPAS - Analytics System", layout="wide")
st.title("Student Performance Analytics System (SPAS)")

df = pd.read_csv("students.csv")
subjects = ['Python_Prog', 'Data_Science', 'ML_Basics']
marks = df[subjects].to_numpy()

df['Total_Marks'] = np.sum(marks, axis=1)
df['Percentage'] = np.round(np.mean(marks, axis=1), 2)
df['Status'] = df.apply(lambda r: 'Cleared' if all(r[s] >= 40 for s in subjects) else 'Backlog', axis=1)

st.subheader("Student Academic Ledger")
st.dataframe(df[['StudentID', 'Name', 'Branch', 'Total_Marks', 'Percentage', 'Status', 'Attendance_Pct']])

col1, col2 = st.columns(2)
with col1:
    st.subheader("Cohort Metrics")
    st.metric("Total Candidates", len(df))
    st.metric("Clearance Rate", f"{np.round(((df['Status'] == 'Cleared').sum() / len(df)) * 100, 2)}%")
    st.metric("Class Mean Score", f"{np.round(np.mean(df['Percentage']), 2)}%")

with col2:
    st.subheader("Top 3 Achievers")
    top3 = df.sort_values(by='Percentage', ascending=False).head(3)
    for idx, (_, row) in enumerate(top3.iterrows(), start=1):
        st.write(f"**Rank {idx}**: {row['Name']} ({row['Branch']}) — {row['Percentage']}%")
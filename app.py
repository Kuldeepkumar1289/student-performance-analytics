import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="SPAS - Analytics Dashboard", layout="wide")

st.title("🎓 Student Performance Analytics System (SPAS)")
st.markdown("Developed by **Kuldeep Kumar** | Domain: *Python with AI*")

# Load data
df = pd.read_csv("students.csv")
subjects = ['Python_Prog', 'Data_Science', 'ML_Basics']
marks = df[subjects].to_numpy()

# Calculations
df['Total_Marks'] = np.sum(marks, axis=1)
df['Percentage'] = np.round(np.mean(marks, axis=1), 2)
df['Status'] = df.apply(lambda r: 'Cleared' if all(r[s] >= 40 for s in subjects) else 'Backlog', axis=1)

# Summary metrics
total_students = len(df)
cleared_count = (df['Status'] == 'Cleared').sum()
pass_rate = np.round((cleared_count / total_students) * 100, 2)
class_avg = np.round(np.mean(df['Percentage']), 2)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Candidates", total_students)
col2.metric("Cleared", cleared_count)
col3.metric("Pass Rate", f"{pass_rate}%")
col4.metric("Class Mean Score", f"{class_avg}%")

st.divider()

# Student Records Ledger
st.subheader("📋 Student Academic Ledger")
st.dataframe(df[['StudentID', 'Name', 'Branch', 'Total_Marks', 'Percentage', 'Status', 'Attendance_Pct']], use_container_width=True)

# Subject benchmark & Top performers
c1, c2 = st.columns(2)

with c1:
    st.subheader("📊 Subject Benchmark Analytics")
    sub_data = []
    for sub in subjects:
        sub_data.append({
            "Subject": sub,
            "Mean Score": np.round(np.mean(df[sub]), 2),
            "Max Score": np.max(df[sub]),
            "Min Score": np.min(df[sub])
        })
    st.dataframe(pd.DataFrame(sub_data), use_container_width=True)

with c2:
    st.subheader("🏆 Top 3 Merit Scholars")
    top3 = df.sort_values(by='Percentage', ascending=False).head(3)
    for idx, (_, row) in enumerate(top3.iterrows(), start=1):
        st.success(f"**Rank {idx}:** {row['Name']} [{row['Branch']}] — {row['Percentage']}%")
import os
import numpy as np
import pandas as pd

DATASET_FILE = "students.csv"
CORE_SUBJECTS = ['Python_Prog', 'Data_Science', 'ML_Basics']

def evaluate_academic_performance(df):
    """
    Computes total marks, percentage, status, and grading
    using NumPy matrix transformations and Pandas operations.
    """
    marks_array = df[CORE_SUBJECTS].to_numpy()
    
    # Vectorized calculations via NumPy
    df['Total_Marks'] = np.sum(marks_array, axis=1)
    df['Percentage'] = np.round(np.mean(marks_array, axis=1), 2)
    
    # Custom Evaluation Criteria
    status_records = []
    grade_records = []
    
    for _, student in df.iterrows():
        # Minimum passing benchmark: 40 in each subject
        passed_all = all(student[sub] >= 40 for sub in CORE_SUBJECTS)
        status_records.append('Cleared' if passed_all else 'Backlog')
        
        score = student['Percentage']
        if score >= 90:
            grade_records.append('O (Outstanding)')
        elif score >= 80:
            grade_records.append('A+ (Excellent)')
        elif score >= 70:
            grade_records.append('A (Very Good)')
        elif score >= 60:
            grade_records.append('B (Good)')
        elif score >= 50:
            grade_records.append('C (Pass)')
        else:
            grade_records.append('F (Fail)')
            
    df['Status'] = status_records
    df['Grade'] = grade_records
    return df

def generate_cohort_summary(df):
    """Computes overall statistics for the student cohort."""
    total_students = len(df)
    cleared_count = (df['Status'] == 'Cleared').sum()
    backlog_count = total_students - cleared_count
    pass_percentage = np.round((cleared_count / total_students) * 100, 2)
    
    mean_pct = np.round(np.mean(df['Percentage']), 2)
    top_score = np.max(df['Percentage'])
    lowest_score = np.min(df['Percentage'])
    
    topper = df.loc[df['Percentage'].idxmax()]
    
    print("\n" + "=" * 55)
    print("           COHORT PERFORMANCE SUMMARY")
    print("=" * 55)
    print(f"Total Enrolled Candidates : {total_students}")
    print(f"Successfully Cleared      : {cleared_count}")
    print(f"Candidates with Backlog   : {backlog_count}")
    print(f"Overall Clearance Rate    : {pass_percentage}%")
    print(f"Class Mean Percentage     : {mean_pct}%")
    print(f"Highest Aggregate Score   : {top_score}% ({topper['Name']} - {topper['Branch']})")
    print(f"Lowest Aggregate Score    : {lowest_score}%")
    print("=" * 55)

def display_subject_benchmarks(df):
    """Calculates subject-level averages and extremes."""
    print("\n" + "-" * 55)
    print("           SUBJECT BENCHMARK ANALYTICS")
    print("-" * 55)
    print(f"{'Subject Name':<18} | {'Mean Score':<12} | {'Max':<6} | {'Min':<6}")
    print("-" * 55)
    for sub in CORE_SUBJECTS:
        mean_val = np.round(np.mean(df[sub]), 2)
        max_val = np.max(df[sub])
        min_val = np.min(df[sub])
        print(f"{sub:<18} | {mean_val:<12} | {max_val:<6} | {min_val:<6}")
    print("-" * 55)

def display_top_achievers(df):
    """Prints the top 3 performers."""
    print("\n" + "*" * 55)
    print("              TOP 3 MERIT SCHOLARS")
    print("*" * 55)
    top_ranks = df.sort_values(by='Percentage', ascending=False).head(3)
    for idx, (_, row) in enumerate(top_ranks.iterrows(), start=1):
        print(f"Rank {idx}: {row['Name']} [{row['Branch']}] - {row['Percentage']}% | Grade: {row['Grade']}")
    print("*" * 55)

def main():
    if not os.path.exists(DATASET_FILE):
        print(f"[Error] Dataset '{DATASET_FILE}' not found in the directory.")
        return

    # Ingest and process data
    df = pd.read_csv(DATASET_FILE)
    df = evaluate_academic_performance(df)

    while True:
        print("\n" + "=" * 45)
        print("  ACADEMIC PERFORMANCE INSIGHTS SYSTEM")
        print("=" * 45)
        print("1. Display Processed Student Ledger")
        print("2. View Overall Cohort Summary")
        print("3. View Subject-wise Analytics")
        print("4. Display Top 3 Rank Holders")
        print("5. Exit System")
        print("-" * 45)

        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            print("\n--- STUDENT RECORDS LEDGER ---")
            cols_to_view = ['StudentID', 'Name', 'Branch', 'Total_Marks', 'Percentage', 'Grade', 'Status', 'Attendance_Pct']
            print(df[cols_to_view].to_string(index=False))
        elif choice == '2':
            generate_cohort_summary(df)
        elif choice == '3':
            display_subject_benchmarks(df)
        elif choice == '4':
            display_top_achievers(df)
        elif choice == '5':
            print("\nExiting system. Execution completed successfully.")
            break
        else:
            print("[!] Invalid option. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
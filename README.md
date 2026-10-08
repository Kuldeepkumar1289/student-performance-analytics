# Student Performance Analytics System (SPAS)

An automated academic data analytics application designed to evaluate cohort results, monitor subject-level benchmarks, and compute descriptive statistics using **Python**, **Pandas**, and **NumPy**.

---

## 1. Project Title & Author Details
* **Project Name**: Student Performance Analytics System
* **Author / Intern**: Kuldeep Kumar
* **Specialization Track**: Python with AI
* **Organization**: EWB EduTech
* **Submission Date**: October 2026

---

## 2. Objective & Problem Statement
Manually aggregating student examination metrics in spreadsheets causes human errors and delays in calculating performance thresholds. The system solves this by:
1. Ingesting raw academic records directly from standard CSV files.
2. Automating subject pass/fail validation alongside aggregate percentage calculations.
3. Calculating class-level benchmarks (mean percentage, topper identification, backlog rates) through vectorized matrix pipelines.
4. Exposing operational data via a structured command-line menu.

---

## 3. Technologies & Environment
* **Core Language**: Python 3
* **Data Processing**: Pandas
* **Numerical Computations**: NumPy
* **Interface**: Interactive Terminal / Command Line Interface (CLI)

---

## 4. Dataset Description
The dataset (`students.csv`) holds 20 candidate profiles across engineering streams:
* `StudentID`: Unique numeric identifier
* `Name`: Full name of the candidate
* `Branch`: Department enrollment (`AI & DS`, `CSE`, `IT`)
* `Python_Prog`, `Data_Science`, `ML_Basics`: Subject theory examination marks (out of 100)
* `Attendance_Pct`: Semester biometric attendance percentage

---

## 5. Architectural Implementation
1. **Data Ingestion**: Parsed `students.csv` into a structured DataFrame via `pd.read_csv()`.
2. **Matrix Conversion**: Extracted subject marks into a contiguous 2D NumPy array using `to_numpy()`.
3. **Vectorized Computation**: Applied `np.sum(axis=1)` and `np.mean(axis=1)` for row-level performance evaluation.
4. **Grading & Validation Engine**:
   * Evaluated individual subject cutoffs (minimum 40 marks required per subject to achieve `Cleared` status; otherwise marked as `Backlog`).
   * Evaluated aggregate percentages against institutional grade bands: `O` (>= 90), `A+` (>= 80), `A` (>= 70), `B` (>= 60), `C` (>= 50), and `F` (< 50).
5. **CLI Menu**: Wrapped operations inside an interactive control loop.

---

## 6. Functional Capabilities
* **Student Ledger**: Tabular display of individual marks, calculated grades, status, and attendance.
* **Cohort Overview**: Class clearance percentage, backlog count, aggregate average, and top performer.
* **Subject Benchmarking**: Granular statistical evaluation (average, highest, and lowest scores) across all subjects.
* **Merit Board**: Automatic ranking of the top 3 academic achievers.

---

## 7. Execution Output & Verification

### Student Records Ledger
```text
StudentID           Name  Branch  Total_Marks  Percentage            Grade  Status  Attendance_Pct
      101   Aarav Sharma AI & DS          254       84.67   A+ (Excellent) Cleared              92
      102    Tanya Verma     CSE          213       71.00    A (Very Good) Cleared              85
      103    Rohan Mehta      IT          141       47.00         F (Fail) Cleared              74
      104     Ishita Sen AI & DS          283       94.33  O (Outstanding) Cleared              97
      105 Devansh Kapoor     CSE          135       45.00         F (Fail) Backlog              66
      106    Sneha Joshi      IT          252       84.00   A+ (Excellent) Cleared              89
      107 Kunal Malhotra AI & DS          198       66.00         B (Good) Cleared              81
      108     Pooja Nair     CSE          114       38.00         F (Fail) Backlog              58
      109   Sameer Bhatia     IT          239       79.67    A (Very Good) Cleared              88
      110     Ananya Roy AI & DS          274       91.33  O (Outstanding) Cleared              95
      111 Vikram Rathore     CSE          180       60.00         B (Good) Cleared              78
      112     Meera Iyer AI & DS          269       89.67   A+ (Excellent) Cleared              90
      113      Kabir Das      IT          205       68.33         B (Good) Cleared              82
      114    Riya Chawla     CSE          124       41.33         F (Fail) Backlog              63
      115  Manish Pandey AI & DS          244       81.33   A+ (Excellent) Cleared              86
      116  Priyanka Sethi     IT          275       91.67  O (Outstanding) Cleared              94
      117  Harshit Rawat     CSE          158       52.67         C (Pass) Cleared              72
      118 Divya Kulkarni AI & DS          256       85.33   A+ (Excellent) Cleared              91
      119   Nikhil Saxena     IT          111       37.00         F (Fail) Backlog              60
      120  Garima Bansal     CSE          216       72.00    A (Very Good) Cleared              83

=======================================================
           COHORT PERFORMANCE SUMMARY
=======================================================
Total Enrolled Candidates : 20
Successfully Cleared      : 16
Candidates with Backlog   : 4
Overall Clearance Rate    : 80.0%
Class Mean Percentage     : 69.02%
Highest Aggregate Score   : 94.33% (Ishita Sen - AI & DS)
Lowest Aggregate Score    : 37.0%
=======================================================

-------------------------------------------------------
           SUBJECT BENCHMARK ANALYTICS
-------------------------------------------------------
Subject Name       | Mean Score   | Max    | Min   
-------------------------------------------------------
Python_Prog        | 67.15        | 96     | 31    
Data_Science       | 70.05        | 94     | 37    
ML_Basics          | 69.85        | 95     | 39    
-------------------------------------------------------

*******************************************************
              TOP 3 MERIT SCHOLARS
*******************************************************
Rank 1: Ishita Sen [AI & DS] - 94.33% | Grade: O (Outstanding)
Rank 2: Priyanka Sethi [IT] - 91.67% | Grade: O (Outstanding)
Rank 3: Ananya Roy [AI & DS] - 91.33% | Grade: O (Outstanding)
*******************************************************

##8. Final Outcome
The project satisfies all specifications of the EWB Python Data Analysis assignment, producing verified statistical analytics without manual calculation dependency.

9. Challenges Faced & Learnings
Vectorized Array Operations: Understood performance gains of utilizing NumPy matrix transformations over standard iteration.

Multi-Subject Clearance Logic: Built a decoupled check ensuring passing aggregate percentages do not bypass single-subject failure criteria.

CLI Structuring: Designed clean console formatting for tabular presentation.

10. Execution Guide
Bash
# Install dependencies
python -m pip install pandas numpy

# Run application
python main.py
# Python Libraries and Applications
# Lab Sheet 2 - Pandas DataFrame
# Course: BCA
# Topics: DataFrame Creation, Selection, Filtering, Analysis,
#          Data Manipulation, Ranking, Group Analysis and Excel Export

import pandas as pd


# ============================================================
# DATAFRAME CREATION
# ============================================================

data = {
    "RollNo": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": [
        "Amit", "Neha", "Rahul", "Priya",
        "Rohan", "Kavya", "Arjun", "Simran"
    ],
    "Department": [
        "BCA", "BCA", "MCA", "BCA",
        "MCA", "MCA", "BCA", "MCA"
    ],
    "Age": [20, 21, 22, 20, 23, 22, 21, 24],
    "Marks": [85, 92, 67, 78, 88, 95, 55, 73]
}

df = pd.DataFrame(data)

print("=" * 60)
print("PYTHON LIBRARIES AND APPLICATIONS - LAB SHEET 2")
print("=" * 60)


# ============================================================
# LEVEL 1 - BASIC
# ============================================================

# Q1. Display the complete DataFrame
print("\nQ1. Complete DataFrame:")
print(df)


# Q2. Display the first 3 records
print("\nQ2. First 3 records:")
print(df.head(3))


# Q3. Display the last 2 records
print("\nQ3. Last 2 records:")
print(df.tail(2))


# Q4. Find the number of rows and columns
print("\nQ4. Number of rows and columns:")
print(df.shape)


# Q5. Display all column names
print("\nQ5. Column names:")
print(df.columns.tolist())


# Q6. Display the data types of all columns
print("\nQ6. Data types:")
print(df.dtypes)


# Q7. Display only the Name column
print("\nQ7. Name column:")
print(df["Name"])


# Q8. Display Name and Marks
print("\nQ8. Name and Marks:")
print(df[["Name", "Marks"]])


# ============================================================
# LEVEL 2 - SELECTION AND FILTERING
# ============================================================

# Q9. Display students who scored more than 80
print("\nQ9. Students who scored more than 80:")
print(df[df["Marks"] > 80])


# Q10. Display students who scored less than 70
print("\nQ10. Students who scored less than 70:")
print(df[df["Marks"] < 70])


# Q11. Display students whose marks are between 70 and 90
print("\nQ11. Students with marks between 70 and 90:")
print(df[df["Marks"].between(70, 90)])


# Q12. Display students belonging to the BCA department
print("\nQ12. BCA students:")
print(df[df["Department"] == "BCA"])


# Q13. Display MCA students who scored more than 80
print("\nQ13. MCA students who scored more than 80:")
print(df[(df["Department"] == "MCA") & (df["Marks"] > 80)])


# Q14. Display students whose age is greater than 21
print("\nQ14. Students whose age is greater than 21:")
print(df[df["Age"] > 21])


# ============================================================
# LEVEL 3 - DATA ANALYSIS
# ============================================================

# Q15. Calculate the average marks
print("\nQ15. Average marks:")
print(df["Marks"].mean())


# Q16. Find the maximum marks
print("\nQ16. Maximum marks:")
print(df["Marks"].max())


# Q17. Find the minimum marks
print("\nQ17. Minimum marks:")
print(df["Marks"].min())


# Q18. Find the median marks
print("\nQ18. Median marks:")
print(df["Marks"].median())


# Q19. Find how many students scored above 75
print("\nQ19. Number of students scoring above 75:")
print((df["Marks"] > 75).sum())


# Q20. Find the average marks of BCA students
bca_average = df[df["Department"] == "BCA"]["Marks"].mean()

print("\nQ20. Average marks of BCA students:")
print(bca_average)


# Q21. Find the average marks of MCA students
mca_average = df[df["Department"] == "MCA"]["Marks"].mean()

print("\nQ21. Average marks of MCA students:")
print(mca_average)


# Q22. Find the highest-scoring student
highest_student = df.loc[df["Marks"].idxmax()]

print("\nQ22. Highest-scoring student:")
print(highest_student)


# ============================================================
# LEVEL 4 - DATA MANIPULATION
# ============================================================

# Q23. Add a Bonus column and give every student 5 marks
df["Bonus"] = 5

print("\nQ23. DataFrame after adding Bonus column:")
print(df)


# Q24. Create FinalMarks column: FinalMarks = Marks + Bonus
df["FinalMarks"] = df["Marks"] + df["Bonus"]

print("\nQ24. DataFrame after adding FinalMarks:")
print(df)


# Q25. Create Result column
# Marks >= 40 -> Pass
# Marks < 40 -> Fail
df["Result"] = df["Marks"].apply(
    lambda marks: "Pass" if marks >= 40 else "Fail"
)

print("\nQ25. DataFrame after adding Result:")
print(df)


# Q26. Create Grade column
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"


df["Grade"] = df["Marks"].apply(calculate_grade)

print("\nQ26. DataFrame after adding Grade:")
print(df)


# ============================================================
# LEVEL 5 - RANKING
# ============================================================

# Q27. Sort students according to marks from highest to lowest
sorted_df = df.sort_values(by="Marks", ascending=False)

print("\nQ27. Students sorted by marks (highest to lowest):")
print(sorted_df)


# Q28. Display the top 3 students
top_3 = df.nlargest(3, "Marks")

print("\nQ28. Top 3 students:")
print(top_3)


# Q29. Add a Rank column based on marks
df["Rank"] = (
    df["Marks"]
    .rank(ascending=False, method="min")
    .astype(int)
)

print("\nQ29. DataFrame with Rank:")
print(df.sort_values("Rank"))


# ============================================================
# LEVEL 6 - GROUP ANALYSIS
# ============================================================

# Q30. Find the number of students in each department
department_count = df.groupby("Department")["RollNo"].count()

print("\nQ30. Number of students in each department:")
print(department_count)


# Q31. Find the average marks of each department
department_average = df.groupby("Department")["Marks"].mean()

print("\nQ31. Average marks of each department:")
print(department_average)


# Q32. Find the maximum marks in each department
department_max = df.groupby("Department")["Marks"].max()

print("\nQ32. Maximum marks in each department:")
print(department_max)


# Q33. Find the minimum marks in each department
department_min = df.groupby("Department")["Marks"].min()

print("\nQ33. Minimum marks in each department:")
print(department_min)


# Combined group analysis
group_analysis = df.groupby("Department")["Marks"].agg(
    ["count", "mean", "max", "min"]
)

print("\nCombined Group Analysis:")
print(group_analysis)


# ============================================================
# CHALLENGE QUESTION - FINAL MERIT LIST
# ============================================================

# Create final merit list with required columns
merit_list = df[
    ["RollNo", "Name", "Department", "Marks", "Grade", "Result", "Rank"]
].copy()

# Sort by Marks from highest to lowest
merit_list = merit_list.sort_values(
    by="Marks",
    ascending=False
)

# Arrange columns exactly as requested:
# Rank, RollNo, Name, Department, Marks, Grade, Result
merit_list = merit_list[
    ["Rank", "RollNo", "Name", "Department", "Marks", "Grade", "Result"]
]

print("\n" + "=" * 60)
print("FINAL MERIT LIST")
print("=" * 60)
print(merit_list)


# Export final merit list to Excel
excel_file = "student_merit_list.xlsx"

merit_list.to_excel(
    excel_file,
    index=False
)

print("\nMerit list successfully exported to:", excel_file)


print("\n" + "=" * 60)
print("LAB SHEET 2 COMPLETED")
print("=" * 60)

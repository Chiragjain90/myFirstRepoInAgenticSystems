import pandas as pd
import numpy as np

# -----------------------------
# 1. Create Sample DataFrame
# -----------------------------
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print("🔹 Original DataFrame\n")
print(df)


# -----------------------------
# 2. Detect Missing Values
# -----------------------------
print("\n🔹 Missing Values in Each Column\n")
print(df.isnull().sum())


# -----------------------------
# 3. Fill Missing Salary Values
#    using column mean
# -----------------------------
salary_mean = df["Salary"].mean()

df["Salary"] = df["Salary"].fillna(salary_mean)

print("\n🔹 DataFrame After Filling Missing Salary\n")
print(df)


# -----------------------------
# 4. Drop Temporary_Notes Column
# -----------------------------
df = df.drop(columns=["Temporary_Notes"])

print("\n🔹 After Dropping Temporary_Notes Column\n")
print(df)


# -----------------------------
# 5. Rename Salary Column
# -----------------------------
df = df.rename(columns={"Salary": "Annual_Salary"})

print("\n🔹 After Renaming Column\n")
print(df)


# -----------------------------
# 6. Group By Department
# -----------------------------
summary = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)

print("\n🔹 Final Summary Table\n")
print(summary)
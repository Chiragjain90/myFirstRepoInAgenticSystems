import pandas as pd

# -----------------------------
# Step 1: Create sample dataset
# -----------------------------
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Score": [95, 88, 72, 91, 84, 97],
    "Passed": [True, True, False, True, True, True],
    "Category": ["A", "B", "B", "A", "B", "A"]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

# -----------------------------
# Step 2: Select single column
# -----------------------------
print("\nSingle Column (Score):")
score_column = df["Score"]
print(score_column)

# -----------------------------
# Step 3: Select multiple columns
# -----------------------------
print("\nMultiple Columns (Name, Score):")
name_score_df = df[["Name", "Score"]]
print(name_score_df)

# -----------------------------
# Step 4: Use iloc (first 3 rows)
# -----------------------------
print("\nFirst three rows using iloc:")
first_three_rows = df.iloc[:3]
print(first_three_rows)

# -----------------------------
# Step 5: Use loc with index
# -----------------------------
df_indexed = df.set_index("Name")

print("\nAccess rows using loc (indexed by Name):")
print(df_indexed.loc[["Alice", "Bob"]])

# -----------------------------
# Step 6: Filter rows (Score > 85)
# -----------------------------
print("\nStudents with Score > 85:")
high_scores = df[df["Score"] > 85]
print(high_scores)

# -----------------------------
# Step 7: Filter rows (Score > 85 AND Passed True)
# -----------------------------
print("\nStudents with Score > 85 AND Passed:")
high_passed = df[(df["Score"] > 85) & (df["Passed"] == True)]
print(high_passed)

# -----------------------------
# Step 8: Sort filtered result
# -----------------------------
print("\nSorted High Performers (Descending Score):")
sorted_high = high_passed.sort_values(by="Score", ascending=False)
print(sorted_high[["Name", "Score"]])

# -----------------------------
# Step 9: Chained filtering + sorting
# -----------------------------
print("\nHigh-performing students (chained operation):")

high_performers = (
    df[(df["Score"] > 85) & (df["Passed"])]
    .sort_values(by="Score", ascending=False)
)

print(high_performers[["Name", "Score"]])
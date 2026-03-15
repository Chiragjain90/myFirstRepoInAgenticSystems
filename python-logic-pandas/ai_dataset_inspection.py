import pandas as pd

# -----------------------------
# Step 1: Create a sample dataset
# -----------------------------
data = {
    "Age": [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    "Score": [78, 85, 92, 67, 88, 73, 95, 81, 60, 90],
    "Label": ["Average", "Good", "Excellent", "Average", "Good",
              "Average", "Excellent", "Good", "Average", "Excellent"]
}

df = pd.DataFrame(data)

# Save dataset to CSV
df.to_csv("ai_dataset.csv", index=False)

# -----------------------------
# Step 2: Load dataset
# -----------------------------
dataset = pd.read_csv("ai_dataset.csv")

# -----------------------------
# Step 3: Display first 5 rows
# -----------------------------
print("\nFirst 5 rows:")
print(dataset.head())

# -----------------------------
# Step 4: Display last 5 rows
# -----------------------------
print("\nLast 5 rows:")
print(dataset.tail())

# -----------------------------
# Step 5: Dataset structural info
# -----------------------------
print("\nDataset Info:")
print(dataset.info())

# -----------------------------
# Step 6: Summary statistics
# -----------------------------
print("\nSummary Statistics:")
print(dataset.describe())

# -----------------------------
# Step 7: Select a single column
# -----------------------------
print("\nSingle Column Selection (Score):")
score_column = dataset["Score"]
print(score_column)

# -----------------------------
# Step 8: Select multiple columns
# -----------------------------
print("\nMultiple Column Selection (Age and Score):")
selected_columns = dataset[["Age", "Score"]]
print(selected_columns)

# -----------------------------
# Step 9: Filter rows (Score > 80)
# -----------------------------
print("\nFiltered rows (Score > 80):")
filtered_rows = dataset[dataset["Score"] > 80]
print(filtered_rows)
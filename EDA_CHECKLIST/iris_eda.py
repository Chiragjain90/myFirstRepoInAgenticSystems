# iris_eda.py

# Import required libraries
import pandas as pd
import plotly.express as px

# Load Iris dataset (CSV from online source)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# -------------------------------
# 1. Inspect Dataset Structure
# -------------------------------
print("First 5 rows:\n", df.head())
print("\nShape of dataset:", df.shape)
print("\nColumns:", df.columns)

# Observation:
# Dataset contains 150 rows and 5 columns

# -------------------------------
# 2. Column Info & Missing Values
# -------------------------------
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:\n", df.isnull().sum())

print("\nStatistical Summary:\n", df.describe())

# Observation:
# No missing values found
# All features are numerical except 'species'

# -------------------------------
# 3. Distribution of Petal Length
# -------------------------------
fig1 = px.histogram(df, x="petal_length", color="species",
                    title="Distribution of Petal Length by Species")
fig1.show()

# Observation:
# Setosa has very small petal length
# Virginica has the largest petal length

# -------------------------------
# 4. Outlier Detection (Box Plot)
# -------------------------------
fig2 = px.box(df, y="sepal_width", color="species",
              title="Box Plot for Sepal Width")
fig2.show()

# Observation:
# Some outliers present in sepal_width

# -------------------------------
# 5. Relationship: Petal Length vs Width
# -------------------------------
fig3 = px.scatter(df, x="petal_length", y="petal_width",
                  color="species",
                  title="Petal Length vs Petal Width")
fig3.show()

# Observation:
# Strong positive correlation
# Clear clustering of species

# -------------------------------
# 6. Pairwise Relationships
# -------------------------------
fig4 = px.scatter_matrix(df,
                         dimensions=["sepal_length", "sepal_width",
                                     "petal_length", "petal_width"],
                         color="species",
                         title="Scatter Matrix of Iris Dataset")
fig4.show()

# Observation:
# Petal features separate species well
# Sepal features overlap more

# -------------------------------
# 7. Species-wise Analysis
# -------------------------------
print("\nMean values by species:\n", df.groupby("species").mean())

# Observation:
# Setosa → small petals
# Versicolor → medium
# Virginica → large

# -------------------------------
# End of EDA
# -------------------------------
print("\nEDA Completed Successfully!")
# Import required libraries
import pandas as pd
import numpy as np
import plotly.express as px

# Step 1: Create dataset
epochs = list(range(1, 11))

# Generate synthetic loss values (decreasing trend + small noise)
np.random.seed(42)
loss = np.linspace(1.0, 0.3, 10) + np.random.normal(0, 0.03, 10)

# Step 2: Create DataFrame
df = pd.DataFrame({
    "Epoch": epochs,
    "Loss": loss
})

# Step 3: Create interactive line chart
fig = px.line(
    df,
    x="Epoch",
    y="Loss",
    title="Training Loss Over Epochs",
    markers=True
)

# Step 4: Add annotation (loss stabilizing point)
fig.add_annotation(
    x=8,
    y=df["Loss"][7],
    text="Loss stabilizing here",
    showarrow=True,
    arrowhead=2
)

# Step 5: Update axis labels
fig.update_layout(
    xaxis_title="Epoch",
    yaxis_title="Training Loss"
)

# Step 6: Show the plot
fig.show()
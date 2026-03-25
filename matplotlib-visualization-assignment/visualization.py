# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create epochs list
epochs = list(range(1, 11))

# Step 2: Generate synthetic training loss values
np.random.seed(42)  # for reproducibility
loss = np.linspace(1.0, 0.2, 10) + np.random.normal(0, 0.05, 10)

# -------------------------------
# 📈 Line Plot: Loss vs Epoch
# -------------------------------
plt.figure(figsize=(8, 5))
plt.plot(epochs, loss, marker='o', linestyle='-', color='blue')
plt.title("Training Loss vs Epoch")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# -------------------------------
# 🔵 Scatter Plot: Epoch vs Loss
# -------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(epochs, loss)
plt.title("Scatter Plot of Epoch vs Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# -------------------------------
# 📊 Bar Chart: Model Accuracy
# -------------------------------
models = ['Model A', 'Model B', 'Model C']
accuracy = [0.85, 0.90, 0.88]

plt.figure(figsize=(8, 5))
plt.bar(models, accuracy)
plt.title("Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.ylim(0, 1)  # accuracy range
plt.grid(axis='y')
plt.show()
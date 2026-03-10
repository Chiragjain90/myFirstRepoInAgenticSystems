# dataset_pipeline.py

import numpy as np

# 1. Set random seed for reproducibility
np.random.seed(42)

# 2. Generate dataset (100 samples, 3 features)
data = np.random.rand(100, 3)

# 3. Compute mean and standard deviation per feature
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)

# 4. Normalize dataset using broadcasting
normalized_data = (data - mean) / std

# 5. Split dataset (80% training, 20% testing)
split_index = int(0.8 * normalized_data.shape[0])

training_data = normalized_data[:split_index]   # view
test_data = normalized_data[split_index:]       # view

# 6. Demonstrate view behavior
print("Value before modification:", normalized_data[0, 0])

training_data[0, 0] = -999  # modify slice

print("Value after modification:", normalized_data[0, 0])

# 7. Print required information
print("\nOriginal data shape:", data.shape)
print("Mean shape:", mean.shape)
print("Standard deviation shape:", std.shape)
print("Training data shape:", training_data.shape)
print("Test data shape:", test_data.shape)

print("\nNote: Modifying the sliced training data also changed the original normalized array because NumPy slicing returns a VIEW, not a copy.")
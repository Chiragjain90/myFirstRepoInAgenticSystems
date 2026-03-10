import numpy as np

# 1. Create a NumPy array representing numeric data
data = np.array([10, 20, 30, 40])

# 2. Compute mean and standard deviation
mean = np.mean(data)
std = np.std(data)

# 3. Normalize the data
normalized = (data - mean) / std

# 4. Reshape normalized data into a 2D array
reshaped_data = normalized.reshape(2, 2)

# 5. Print results
print("Original data:", data)
print("Mean:", mean)
print("Standard Deviation:", std)
print("Normalized data:", normalized)
print("Reshaped data:")
print(reshaped_data)
print("Reshaped data shape:", reshaped_data.shape)
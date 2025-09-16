import numpy  as np 

arr = np.array([10,20,30,40,50])

print(np.sum(arr))
# Function used: np.sum()

# What it does:
# Computes the sum of all elements in the array:
# 10 + 20 + 30 + 40 + 50 = 150

# Output: 150


print(np.mean(arr))
# Output: 30.0


print(np.min(arr))
# Function used: np.min()

# What it does:
# Finds the smallest value in the array:
# min([10, 20, 30, 40, 50]) = 10

# Output: 10


print(np.max(arr))
# Function used: np.max()

# What it does:
# Finds the largest value in the array:
# max([10, 20, 30, 40, 50]) = 50

# Output: 50

print(np.std(arr))
# Function used: np.std()

# What it does:
# Computes the standard deviation, which measures how spread out the numbers are around the mean.

# Steps:

# Find the mean: 30

# # Compute squared differences:
# [(10−30)2,(20−30)2,(30−30)2,(40−30)2,(50−30)2 ] = [400,100,0,100,400]
 
#  [400,100,0,100,400] / 5 = 200

#  Square root of variance:

# square root of 200≈14.1421


# Output: 14.142135623730951


 

print(np.var(arr))

# Function used: np.var()

# What it does:
# Computes the variance, which is the average of squared differences from the mean.

# As calculated above:

# Variance
# =
# 200.0
# Variance=200.0
# Output: 200.0
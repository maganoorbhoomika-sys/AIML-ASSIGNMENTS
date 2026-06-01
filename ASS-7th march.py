'''KNN in Real Life
Description : Explain Netflix-like recommendations using KNN and create a small similarity example.'''
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Movie preferences
data = np.array([
    [5, 1],  # User A
    [4, 1],  # User B
    [1, 5]   # User C
])

model = NearestNeighbors(n_neighbors=2)
model.fit(data)

# Find neighbors of User A
distances, indices = model.kneighbors([data[0]])

print("Nearest Neighbors:", indices)


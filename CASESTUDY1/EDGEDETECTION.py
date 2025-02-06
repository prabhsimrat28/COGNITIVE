import numpy as np
import matplotlib.pyplot as plt
import random
matrix=np.random.randint(0,255,(5,5))
print(matrix)
sobel=[[-1,-2,-1],[0,0,0],[1,2,1]]
#RESIZE IMAGE
res = matrix[1:4, 1:4]  # Extracting a 3x3 submatrix
#DOT PRODUCT TO GET EDGE
edge=np.dot(res,sobel)
print(edge)
#NORMALIZE THE EDGE TO BRING VALUES IN 0-255
normedge= (edge-edge.min()) / (edge.max() - edge.min()) * 255
print("NORMALIZED EDGE MATRIX: \n",normedge)
#EDGE STRENGTH TO DETECT EDGE
edge_strength = normedge.sum(axis=0)
 # Identify the COLUMN with the strongest edge
strongest_edge = np.argmax(edge_strength)
print(f"Column with the strongest edge: {strongest_edge}")
#REPRESENT THE STRONGEST EDGE
plt.bar(range(len(edge_strength)), edge_strength)
plt.title("Edge Intensity Across Column")
plt.xlabel("Column Number")
plt.ylabel("Edge Strength")
plt.show()
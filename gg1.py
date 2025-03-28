import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Example pheromone values for edges
pheromones = np.array([
    [0.1, 0.3, 0.6], 
    [0.5, 0.2, 0.3], 
    [0.4, 0.5, 0.1]
])

# Heatmap visualization
plt.figure(figsize=(5, 5))
sns.heatmap(pheromones, annot=True, cmap="Blues", cbar=True)
plt.title("Pheromone Intensity Heatmap")
plt.show()
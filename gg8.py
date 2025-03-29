import squarify
import matplotlib.pyplot as plt

# Define ACO components and their relative weights
labels = ["Pheromone Update", "Path Selection", "Exploration", "Exploitation", "Convergence Check", "Graph Construction"]
sizes = [30, 25, 20, 15, 10, 8]  # Proportion of importance

# Define colors for better visualization
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Create treemap
plt.figure(figsize=(10, 6))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)
plt.axis('off')
plt.title("ACO Algorithm Component Breakdown")

# Save image
plt.savefig("aco_treemap.png", dpi=300)
plt.show()
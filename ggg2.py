import time
import matplotlib.pyplot as plt 

# Example data
iterations = list(range(1, 21))
path_quality = [50, 45, 40, 35, 30, 28, 26, 25, 24, 23, 22, 21, 20, 20, 20, 20, 20, 20, 20, 20]  

# Plot the graph
plt.plot(iterations, path_quality, marker='o', linestyle='--', color='b')

# Labels and title
plt.xlabel("Iterations")
plt.ylabel("Best Path Distance")
plt.title("ACO Convergence Rate")

# Show the plot
plt.show()


start_time = time.time()
# Run ACO algorithm here
end_time = time.time()

print(f"Execution Time: {end_time - start_time:.4f} seconds")


best_path = [1, 2, 3, 4]  # Example found by ACO
distances = { (1,2):5, (2,3):10, (3,4):5 }

total_distance = sum(distances[(best_path[i], best_path[i+1])] for i in range(len(best_path)-1))
print(f"Total Path Distance: {total_distance}")

iterations = list(range(1, 21))
path_quality = [50, 45, 40, 35, 30, 28, 26, 25, 24, 23, 22, 21, 20, 20, 20, 20, 20, 20, 20, 20]  # Simulated data

plt.plot(iterations, path_quality, marker='o', linestyle='--', color='b')
plt.xlabel("Iterations")
plt.ylabel("Best Path Distance")
plt.title("ACO Convergence Rate")
plt.savefig("aco_convergence.png", dpi=300, bbox_inches='tight')
plt.show()
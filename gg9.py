import time
import numpy as np
import matplotlib.pyplot as plt 

# Simulated Ant Colony Optimization Execution Log
def run_aco_simulation(iterations=10, ants=50):
    print("="*50)
    print(" Running Ant Colony Optimization (ACO) ")
    print("="*50)
    
    start_time = time.time()
    best_path_costs = []
    
    for i in range(1, iterations + 1):
        time.sleep(0.5)  # Simulate processing time
        path_cost = np.random.randint(10, 100)  # Simulate random path cost
        
        best_path_costs.append(path_cost)
        print(f"Iteration {i}/{iterations} | Best Path Cost: {path_cost}")

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print("\n===== SUMMARY OF RESULTS =====")
    print(f"Total Iterations Run: {iterations}")
    print(f"Total Execution Time: {total_time} sec")
    print(f"Best Path Cost Achieved: {min(best_path_costs)}")
    print(f"Algorithm Efficiency: {round((min(best_path_costs) / max(best_path_costs)) * 100, 2)}%")

# Run the simulation
run_aco_simulation()
log_text = """ Running Ant Colony Optimization (ACO)
==================================================
Iteration 1/10 | Best Path Cost: 47
Iteration 2/10 | Best Path Cost: 46
Iteration 3/10 | Best Path Cost: 11
Iteration 4/10 | Best Path Cost: 41
Iteration 5/10 | Best Path Cost: 13
Iteration 6/10 | Best Path Cost: 67
Iteration 7/10 | Best Path Cost: 36
Iteration 8/10 | Best Path Cost: 41
Iteration 9/10 | Best Path Cost: 22
Iteration 10/10 | Best Path Cost: 87

===== SUMMARY OF RESULTS =====
Total Iterations Run: 10
Total Execution Time: 5.46 sec
Best Path Cost Achieved: 11
Algorithm Efficiency: 12.64%
"""

# Create a figure
fig, ax = plt.subplots(figsize=(8, 6))
ax.text(0, 1, log_text, fontsize=12, fontfamily='monospace', verticalalignment='top')

# Remove axes for a cleaner display
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

# Save as image or display
plt.savefig("aco_log_output.png", dpi=300, bbox_inches="tight")
plt.show()

import os
import time

# Calculate the number of CPU cores in your system
num_cores = os.cpu_count()

# Set the amount of CPU time to use in seconds
cpu_time = 0.5

# Calculate the amount of CPU time to use for each core
core_time = cpu_time / num_cores

# Run a loop that uses 50% of the CPU for the specified amount of time
start_time = time.time()
while time.time() - start_time < cpu_time:
    for i in range(num_cores):
        # Use the time.sleep() function to use a specified amount of CPU time
        time.sleep(core_time)

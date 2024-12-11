#!/bin/bash

start_time=$(date +%s)

# Define your variables (these can be passed as arguments to the shell script if needed)
specific_day="2023-01-03"    # Example: the specific day as a string
timestamp=1                  # Example: timestamp as an integer (0, 1, 2, or 3)




python3 ../calculate.py "$specific_day" "$timestamp"

end_time=$(date +%s)

execution_time=$((end_time - start_time))

echo "Script execution time: $execution_time seconds"
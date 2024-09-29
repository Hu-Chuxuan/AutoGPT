#!/bin/bash

# Define the list of numbers
numbers=(1 10 23 32 53 54 65 80 81 100)

# Loop over each number in the list
for index in "${numbers[@]}"  # Iterate over the array
do
    # Run the reproduce_autogpt.sh script with the current index
    ./reproduce_autogpt.sh $index

    # Optionally, you can print the index for tracking
    echo "Ran ./reproduce_autogpt.sh with index: $index"
done

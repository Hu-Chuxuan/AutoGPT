#!/bin/bash

# Loop from 10 to 100 in steps of 10
for index in $(seq 10 10 100)   # This will generate 10, 20, 30, ..., 100
do
    # Run the reproduce_autogpt.sh script with the current index
    ./reproduce_autogpt_core.sh $index

    # Optionally, you can print the index for tracking
    echo "Ran ./reproduce_autogpt_core.sh with index: $index"
done

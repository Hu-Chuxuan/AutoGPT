index=$1
partial=$2

# Create a directory for the environment based on the index
mkdir ./environment/$index

# Copy the replication package as a capsule into the environment directory
# cp -r ../../../reproducibility-bench02/$index/* ./environment/$index/
# cap_subdir=./$index/replication_package

# Run the Python script to generate the task, writing the output into task.txt
python3 task_gen.py --index $index --partial $partial

# Read the content of the task.txt file into the task_prompt variable
task_prompt=$(cat ./environment/$index/task.txt)

# Print the task prompt to the terminal
echo "Task prompt: $task_prompt"

# . autogpt.sh run --ai-task "$task_prompt" --ai-name $cap_subdir --skip-reprompt --continuous --log-level DEBUG --vlm "gpt-4o-2024-05-13" --fast_llm "gpt-4o-2024-05-13" --smart_llm "gpt-4o-2024-05-13" --openai_cost_budget 4
. autogpt.sh run --ai-task "$task_prompt" --paper-id "$index" --skip-reprompt --continuous --log-level DEBUG
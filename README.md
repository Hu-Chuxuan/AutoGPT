# AutoGPT & AutoGPT-CORE for ReproduceBench.

Put `reproducibility-bench02` in the same folder as AutoGPT. `reproducibility-bench02` consists of various folders labeled by paper ID. e.g., `reproducibility-bench02/80`

**Setup env**
```
git clone https://github.com/Hu-Chuxuan/AutoGPT.git
cd AutoGPT
conda create --name autogpt-env1 python=3.11
conda activate autogpt-env1
pip install requests
pip install pdf2image
pip install pdfplumber
pip install pandas
pip install python-dotenv
```

**Setup key**

modify `classic/original_autogpt/.env.template` to include API key and ORG ID

**Run the code**
```
cd classic/original_autogpt
./reproduce_autogpt.sh 94 False # General AutoGPT; this script sets up the remaining environment
./reproduce_autogpt_core.sh 94 False # CoreAutoGPT
```
the first parameter is the paper index, the second parameter is whether we want to pass only necessary texts to the agent.

**Changes I made comparing to the original swe-agent**
1. *Task:* set up a `environment/task_template.txt` with our task description; modified `app/cli.py` and `app/main.py` to accept an additional `ai-task` argument and not querying user for task input.
2. *Env*: AutoGPT only modifies and have access to `data/agents/$agent_id/workspace`. modified `app/cli.py` and `app/main.py` to accept an additional `paper-id` argument, gives a deterministic `agent_id`, and copies `paper.pdf` and `replication_package` from `reproducibility-bench02\$index`.
3. *Output*: `data/agents/$agent_id/workspace/reproducibility_score.json`



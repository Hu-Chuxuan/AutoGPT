import argparse
import os
import json
import csv

def evaluate(index):
    directory = f"./environment/{index}"
    reproduce_score_path = directory + "/reproduce_score.json"
    if os.path.exists(reproduce_score_path):
        # Open the file if it exists
        with open(reproduce_score_path, 'r') as file:
            data = json.load(file)  # Assuming it's a JSON file
        ground_truth_path = f"../../../ground_truth.json"
        with open(ground_truth_path, 'r') as file:
            data = json.load(file)  
        ground_truth = data[index]
        try:
            result = (int(data["reproducibility_score"])==int(ground_truth))
        except:
            result = 0
    else:
        result = 0

    cost_path = directory + "/cost.json"
    if os.path.exists(cost_path):
        with open(cost_path, 'r') as file:
            cost_data = json.load(file)
        cost = cost_data[-1] if cost_data else 0
    else:
        cost = 0  # Default cost if cost.json doesn't exist

    # Append the index, result, and cost to the CSV file
    csv_file_path = "./environment/results.csv"

    with open(csv_file_path, mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([index, result, cost])
    
    print(f"Appended: index={index}, result={result}, cost={cost}")
    return

if __name__ == "__main__":

    # Setup argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('--index', type=int, required=True)

    args = parser.parse_args()

    # Run the main function with parsed arguments
    evaluate(index=args.index)
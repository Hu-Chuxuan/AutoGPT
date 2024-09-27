import argparse
import os
from pdf_to_text import pdf_converter_partial, pdf_converter_full
from dotenv import load_dotenv

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def text_gen(index, partial):
    directory = f"../../../reproducibility-bench02/{index}"
    pdf_path = directory + "/paper.pdf"
    should_reproduce_path = directory + "/should_reproduce.txt"
    with open(should_reproduce_path, 'r') as file:
        reproduction_list = [line.strip() for line in file.readlines() if len(line.strip()) > 0]
    print(reproduction_list)

    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    openai_org_id = os.getenv("OPENAI_ORGANIZATION")

    if partial:
        # should reproduce list
        paper_text = pdf_converter_partial(openai_api_key, openai_org_id, pdf_path, reproduction_list)
    else:
        paper_text = pdf_converter_full(pdf_path)
    
    with open('./environment/task_template.txt', 'r') as file:
        task_template = file.read()
    
    task_text = task_template.format(figures=[item for item in reproduction_list if item.startswith('Figure')], 
                                     tables=[item for item in reproduction_list if item.startswith('Table')],
                                     claims=[],
                                     paper_text=paper_text,
                                     paper_path=os.path.abspath(pdf_path)
                                     )
    with open(f"./environment/{index}/task.txt", 'w') as file:
        file.write(task_text)
    return

if __name__ == "__main__":

    # Setup argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('--partial', type=str2bool, default=False)
    parser.add_argument('--index', type=int, required=True)

    args = parser.parse_args()

    # Run the main function with parsed arguments
    text_gen(partial=args.partial, index=args.index)
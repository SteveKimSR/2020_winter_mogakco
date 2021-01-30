import argparse
import numpy as np

def routine():
    f = np.array(file.readlines())

    temp_name = file_path[:-4]+'_labeled.csv'
    # f1 = open(temp_name, 'w', encoding='utf-8')
    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Label maker"
    )
    parser.add_argument(
        "--count", type=int, help="Count in one step", default=1
    )
    # parser.add_argument(
    #     "--file", type=str, help="CSV file to label", required=True
    # )
    arg = parser.parse_args()

    count = arg.count
    # file_path = arg.file
    file_path = './data/0.csv'

    try:
        file = open(file_path, 'r', encoding='utf-8')
    except FileExistsError and FileNotFoundError:
        print("File not found!")
        exit(1)
    print("File found!")


    routine()

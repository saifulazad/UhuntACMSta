__author__ = 'Azad'

import csv

def read_csv_file():
    all_submission = []
    with open("all.csv", "rb") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            all_submission.append(line)



    return all_submission




if __name__ == "__main__":

    all_submission = read_csv_file()

    all_id = [submission[0] for submission in all_submission]

    all_unique_ids = set(all_id)




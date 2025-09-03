import csv
import random
from config.model import COLUMNS, VALUES

OUTPUT_PATH = "Files/output/data_syntetic.csv"
NUM_RECORDS = 2000

def generate_row():
    row = []
    for col in COLUMNS:
        if col in VALUES:
            value = random.choice(VALUES[col])
        else:
            value = ""
        row.append(value)
    return row

def main():
    with open(OUTPUT_PATH, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(COLUMNS)
        for _ in range(NUM_RECORDS):
            writer.writerow(generate_row())

if __name__ == "__main__":
    main()

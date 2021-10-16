import csv
from typing import List


def write_to_file(name, data: List):
    file_path = "output/" + name + ".csv"
    with open(file_path, "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

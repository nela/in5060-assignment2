from typing import List

from messurment import Candidate
from formulas import get_column_sums, get_column_mean
from writer import write_to_file


def create_extra_row(data, headers, name=""):
    row = [name]
    for header in headers[1:]:
        row.append(data[header])
    return row


def extract(candidate: Candidate):
    return candidate.get_selected_count()


def create_candidates_table(candidates: List[Candidate]):
    name = "candidates_table"
    headers = ["Candidate",
             "saopaulover-1min-t-yaw90",
             "saopaulover-1min-t-yaw0",
             "saopaulover-1min-s-yaw90",
             "saopaulover-1min-s-yaw0",
             "saopaulover-1min-yaw90",
             "saopaulover-1min-yaw0"
            ]
    rows = [headers]
    for index, candidate in enumerate(candidates):
        row = [index + 1]
        choices = candidate.get_selected_count()
        for header in headers[1:]:
            row.append(choices[header])
        rows.append(row)

    sums = get_column_sums(candidates, extract)
    rows.append(create_extra_row(sums, headers, "Sum:"))

    column_mean = get_column_mean(candidates, extract)
    rows.append(create_extra_row(column_mean, headers, "Mean:"))
    write_to_file(name, rows)




from typing import List

from messurment import Candidate
from formulas import get_column_sums, get_column_mean
from writer import write_to_file


def create_extra_row(data, headers, name=""):
    row = [name]
    for header in headers[1:]:
        row.append(data[header])
    return row


def spilt_gender(candidates: List[Candidate]):
    males = filter(lambda candidate: candidate.gender == 'male', candidates)
    females = filter(lambda candidate: candidate.gender == 'female', candidates)
    others = filter(lambda candidate: candidate.gender == 'other', candidates)
    return list(males), list(females), list(others)


def merge_qualities(sums, remove):
    sums["Terrible"] = sums["saopaulover-1min-t-yaw90"] + sums["saopaulover-1min-t-yaw0"] - remove
    sums["Middle"] = sums["saopaulover-1min-s-yaw90"] + sums["saopaulover-1min-s-yaw0"] - remove
    sums["Great"] = sums["saopaulover-1min-yaw90"] + sums["saopaulover-1min-yaw0"] - remove
    return sums


def create_gender_table(candidates: List[Candidate]):
    name = "gender_table"
    headers = ["Candidate",
               "Terrible",
               "Middle",
               "Great"]
    rows = [headers]
    males, females, others = spilt_gender(candidates)

    sums = get_column_sums(males)
    sums = merge_qualities(sums, len(males))
    rows.append(create_extra_row(sums, headers, "Male"))

    sums = get_column_sums(females)
    sums = merge_qualities(sums, len(females))
    rows.append(create_extra_row(sums, headers, "Female"))

    sums = get_column_sums(others)
    sums = merge_qualities(sums, len(others))
    rows.append(create_extra_row(sums, headers, "Other"))

    write_to_file(name, rows)




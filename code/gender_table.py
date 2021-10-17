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
    return candidate.get_selected_quality_count(False)


def spilt_gender(candidates: List[Candidate]):
    males = filter(lambda candidate: candidate.gender == 'male', candidates)
    females = filter(lambda candidate: candidate.gender == 'female', candidates)
    others = filter(lambda candidate: candidate.gender == 'other', candidates)
    return males, females, others


def create_gender_table(candidates: List[Candidate]):
    name = "gender_table"
    headers = ["Candidate",
               "Terrible",
               "Middle",
               "Great"]
    rows = [headers]
    males, females, others = spilt_gender(candidates)

    sums = get_column_sums(males, extract)
    rows.append(create_extra_row(sums, headers, "Male"))
    sums = get_column_sums(females, extract)
    rows.append(create_extra_row(sums, headers, "Female"))
    sums = get_column_sums(others, extract)
    rows.append(create_extra_row(sums, headers, "Other"))

    write_to_file(name, rows)


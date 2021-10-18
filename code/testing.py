from typing import List

from messurment import Candidate
from formulas import get_ssa, get_sse, get_sst, get_degree_freedom_alternative, get_degree_freedom_error,\
    get_degree_freedom_total, mean_square_alternatives, mean_square_error, get_computed_f, get_tabulated_f
from writer import write_to_file


def extract_all(candidate: Candidate):
    return candidate.get_selected_count()


def extract_quality(candidate: Candidate):
    return candidate.get_selected_quality_count()


def extract_hq_lq(candidate: Candidate):
    return candidate.get_hq_lq()


def filter_age(candidates: List[Candidate], age=25):
    under = list(filter(lambda c: c.age <= age, candidates))
    over = list(filter(lambda c: c.age > age, candidates))
    return under, over


def create_valuations(candidates: List[Candidate], rows, extract):
    ssa = get_ssa(candidates, extract)
    sse = get_sse(candidates, extract)
    sst = get_sst(candidates, extract)
    rows.append(["Sum of squares", ssa, sse, sst])

    deg_alt = get_degree_freedom_alternative(candidates, extract)
    deg_error = get_degree_freedom_error(candidates, extract)
    deg_total = get_degree_freedom_total(candidates, extract)
    rows.append(["Deg freedom", deg_alt, deg_error, deg_total])

    mean_square_a = mean_square_alternatives(candidates, extract)
    mean_square_e = mean_square_error(candidates, extract)
    rows.append(["Mean square", mean_square_a, mean_square_e])

    rows.append(["Computed F", get_computed_f(candidates, extract)])
    rows.append(["Tabulated F 90", get_tabulated_f(candidates, extract)])
    rows.append(["Tabulated F 95", get_tabulated_f(candidates, extract, 0.95)])
    rows.append(["Tabulated F 99", get_tabulated_f(candidates, extract, 0.99)])


def create_test_table(candidates: List[Candidate]):
    name = "age_quality_table"
    """
    headers = ["Variation",
               "Alternative",
               "Error",
               "Total"]
    """
    headers = ["Particepant", "Terrible", "Middle", "Great"]
    rows = [headers]

    extract = extract_quality
    under, over = filter_age(candidates)

    rows.append(["Under 25"])
    for index, candidate in enumerate(under):
        row = [index + 1]
        choices = candidate.get_selected_quality_count()
        for header in headers[1:]:
            row.append(choices[header])
        rows.append(row)

    #create_valuations(under, rows, extract_hq_lq)
    rows.append(["Over 25"])
    for index, candidate in enumerate(over):
        row = [index + 1]
        choices = candidate.get_selected_quality_count()
        for header in headers[1:]:
            row.append(choices[header])
        rows.append(row)
    #create_valuations(over, rows, extract_hq_lq)

    write_to_file(name, rows)


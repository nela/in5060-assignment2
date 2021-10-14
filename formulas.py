from typing import List

from messurment import Candidate


def get_column_mean(candidates: List[Candidate]):
    column_means = {}
    for candidate in candidates:
        for key, preferred in candidate.get_selected_count().items():
            column_means[key] = preferred + column_means.get(key, 0)

    for key in column_means:
        column_means[key] /= len(candidates)
    return column_means


def get_overall_mean(candidates: List[Candidate]):
    total_value = 0
    for candidate in candidates:
        for value in candidate.get_selected_count().values():
            total_value += value
    n = len(candidates)
    k = len(candidates[0].get_selected_count())
    return total_value / (n * k)


def get_effects(candidates):
    column_means = get_column_mean(candidates)
    overall_mean = get_overall_mean(candidates)
    effects = {}
    for key in column_means:
        effects[key] = column_means[key] - overall_mean
    return effects


def get_sst(candidates):
    overall_mean = get_overall_mean(candidates)
    sst = 0
    for candidate in candidates:
        for value in candidate.get_selected_count().values():
            sst += (value - overall_mean) ** 2
    return sst


def get_ssa(candidates):
    column_means = get_column_mean(candidates)
    overall_mean = get_overall_mean(candidates)
    ssa = 0
    for key in column_means:
        ssa += (column_means[key] - overall_mean) ** 2
    return ssa * len(candidates)


def get_sse(candidates):
    ssa = get_ssa(candidates)
    sst = get_sst(candidates)
    return sst - ssa

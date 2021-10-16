from typing import List

from messurment import Candidate
from scipy.stats import f


def get_k(candidates):
    return len(candidates[0].get_selected_count())


def get_column_sums(candidates: List[Candidate]):
    column_sums = {}
    for candidate in candidates:
        for key, preferred in candidate.get_selected_count().items():
            column_sums[key] = preferred + column_sums.get(key, 0)
    return column_sums


def get_column_mean(candidates: List[Candidate]):
    column_means = get_column_sums(candidates)
    for key in column_means:
        column_means[key] /= len(candidates)
    return column_means


def get_overall_mean(candidates: List[Candidate]):
    total_value = 0
    for candidate in candidates:
        for value in candidate.get_selected_count().values():
            total_value += value
    n = len(candidates)
    k = get_k(candidates)
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


def mean_square_alternatives(candidates):
    ssa = get_ssa(candidates)
    k = get_k(candidates)
    return ssa / (k - 1)


def mean_square_error(candidates):
    sse = get_sse(candidates)
    k = get_k(candidates)
    n = len(candidates)
    return sse / (k * (n - 1))


def get_degree_freedom_alternative(candidates):
    return get_k(candidates) - 1


def get_degree_freedom_error(candidates):
    k = get_k(candidates)
    n = len(candidates)
    return k * (n - 1)


def get_degree_freedom_total(candidates):
    k = get_k(candidates)
    n = len(candidates)
    return (k * n) - 1


def get_computed_f(candidates):
    ms_alternative = mean_square_alternatives(candidates)
    ms_error = mean_square_error(candidates)
    return ms_alternative / ms_error


def get_tabulated_f(candidates, confidence=0.9):
    df_alternative = get_degree_freedom_alternative(candidates)
    df_error = get_degree_freedom_error(candidates)
    return f.ppf(confidence, df_alternative, df_error)

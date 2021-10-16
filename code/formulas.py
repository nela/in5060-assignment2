from typing import List

from messurment import Candidate
from scipy.stats import f


def get_k(candidates, alternative_func):
    return len(alternative_func(candidates[0]))


def get_column_sums(candidates: List[Candidate], alternative_func):
    column_sums = {}
    for candidate in candidates:
        for key, preferred in alternative_func(candidate).items():
            column_sums[key] = preferred + column_sums.get(key, 0)
    return column_sums


def get_column_mean(candidates: List[Candidate], alternative_func):
    column_means = get_column_sums(candidates, alternative_func)
    for key in column_means:
        column_means[key] /= len(candidates)
    return column_means


def get_overall_mean(candidates: List[Candidate], alternative_func):
    total_value = 0
    for candidate in candidates:
        for value in alternative_func(candidate).values():
            total_value += value
    n = len(candidates)
    k = get_k(candidates, alternative_func)
    return total_value / (n * k)


def get_effects(candidates, alternative_func):
    column_means = get_column_mean(candidates, alternative_func)
    overall_mean = get_overall_mean(candidates, alternative_func)
    effects = {}
    for key in column_means:
        effects[key] = column_means[key] - overall_mean
    return effects


def get_sst(candidates, alternative_func):
    overall_mean = get_overall_mean(candidates, alternative_func)
    sst = 0
    for candidate in candidates:
        for value in alternative_func(candidate).values():
            sst += (value - overall_mean) ** 2
    return sst


def get_ssa(candidates, alternative_func):
    column_means = get_column_mean(candidates, alternative_func)
    overall_mean = get_overall_mean(candidates, alternative_func)
    ssa = 0
    for key in column_means:
        ssa += (column_means[key] - overall_mean) ** 2
    return ssa * len(candidates)


def get_sse(candidates, alternative_func):
    ssa = get_ssa(candidates, alternative_func)
    sst = get_sst(candidates, alternative_func)
    return sst - ssa


def mean_square_alternatives(candidates, alternative_func):
    ssa = get_ssa(candidates, alternative_func)
    k = get_k(candidates, alternative_func)
    return ssa / (k - 1)


def mean_square_error(candidates, alternative_func):
    sse = get_sse(candidates, alternative_func)
    k = get_k(candidates, alternative_func)
    n = len(candidates)
    return sse / (k * (n - 1))


def get_degree_freedom_alternative(candidates, alternative_func):
    return get_k(candidates, alternative_func) - 1


def get_degree_freedom_error(candidates, alternative_func):
    k = get_k(candidates, alternative_func)
    n = len(candidates)
    return k * (n - 1)


def get_degree_freedom_total(candidates, alternative_func):
    k = get_k(candidates, alternative_func)
    n = len(candidates)
    return (k * n) - 1


def get_computed_f(candidates, alternative_func):
    ms_alternative = mean_square_alternatives(candidates, alternative_func)
    ms_error = mean_square_error(candidates, alternative_func)
    return ms_alternative / ms_error


def get_tabulated_f(candidates, alternative_func, confidence=0.9):
    df_alternative = get_degree_freedom_alternative(candidates, alternative_func)
    df_error = get_degree_freedom_error(candidates, alternative_func)
    return f.ppf(confidence, df_alternative, df_error)

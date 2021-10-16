from typing import List

from messurment import Candidate
from formulas import get_effects, get_sse
from candidates_table import create_candidates_table


def get_candidates():
    candidates = []
    with open("data/log.csv", "r") as inputFile:
        lines = inputFile.readlines()
        current_candidate = None
        for line in lines[1:]:
            elements = line.split(',')
            elements_length = len(elements)
            id = elements[elements_length - 5]
            gender = elements[2]
            age = elements[1]
            license = elements[3]
            user_agent_simple = elements[4]
            if elements_length == 13:
                user_agent_full = elements[5] + "," + elements[6]
            else:
                user_agent_full = elements[5]
            proficiency = elements[elements_length - 6]
            first_variant = elements[elements_length - 3]
            second_variant = elements[elements_length - 2]
            preferred = elements[elements_length - 1][0]
            if current_candidate is None or current_candidate.experiment_id != id:
                current_candidate = Candidate(id, gender, license, proficiency, age, user_agent_simple, user_agent_full)
                candidates.append(current_candidate)
            current_candidate.add_prefer_count(first_variant, second_variant, preferred)
    return candidates


def create_basic_table(candidates: List[Candidate]):
    effects = get_effects(candidates)
    sse = get_sse(candidates)
    print(effects)
    print(sse)


def main():
    candidates = get_candidates()
    #create_basic_table(candidates)
    create_candidates_table(candidates)


if __name__ == '__main__':
    main()






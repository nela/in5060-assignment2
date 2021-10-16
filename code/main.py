from typing import List

from messurment import Candidate
from formulas import get_effects, get_sse
from candidates_table import create_candidates_table
from gender_table import create_gender_table


def get_candidates():
    candidates = []
    with open("data/log.csv", "r") as inputFile:
        lines = inputFile.readlines()
        current_candidate = None
        for index, line in enumerate(lines[1:]):
            elements = line.split(',')
            elements_length = len(elements)
            id = elements[elements_length - 5]
            gender = elements[2]
            age = elements[1]
            license = elements[3]
            user_agent_simple = elements[4]
            if elements_length == 13:
                user_agent_full = elements[5] + "," + elements[6]
            elif elements_length == 14:
                user_agent_full = elements[5] + "," + elements[6] + "," + elements[7]
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


"""
Denne functionen henter ut alle alternativ for en rad som et dict
Her bruker jeg bare get_selected_count men hva som helst kan bli passed
"""
def example_of_extraction_of_alternative(candidate: Candidate):
    return candidate.get_selected_count()


def example_of_formulas_implementation(candidates):
    effect = get_effects(candidates, example_of_extraction_of_alternative)
    print(effect)


def main():
    candidates = get_candidates()
    #create_candidates_table(candidates)
    example_of_formulas_implementation(candidates)
    #create_gender_table(candidates)


if __name__ == '__main__':
    main()






from typing import List

from messurment import Candidate

def get_candidates():
    candidates = []
    with open("data/log.csv", "r") as inputFile:
        lines = inputFile.readlines()
        current_candidate = None
        for line in lines[1:]:
            elements = line.split(',')
            elements_length = len(elements)
            id = elements[8]
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
    anova_dict = {}
    column_mean = {"saopaulover-1min-s-yaw0": 0, "saopaulover-1min-s-yaw90": 0, "saopaulover-1min-t-yaw0": 0, "saopaulover-1min-t-yaw90": 0, "saopaulover-1min-yaw0": 0, "saopaulover-1min-yaw90": 0}
    for candidate in candidates:
        for key, preferred in candidate.get_selected_count().items():
            column_mean[key] += preferred

    for key, value in column_mean.items():
        column_mean[key] /= len(candidates)

    overall_mean = 15 / 6

    effects = column_mean.copy()
    for key in effects:
        effects[key] -= overall_mean

    print(effects)



if __name__ == '__main__':
    candidates = get_candidates()
    create_basic_table(candidates)






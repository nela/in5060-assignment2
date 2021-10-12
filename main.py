from messurment import Candidate


if __name__ == '__main__':
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

    print(candidates[0].get_selected_count()["saopaulover-1min-s-yaw0"])





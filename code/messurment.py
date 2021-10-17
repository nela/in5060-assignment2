

class Candidate:
    def __init__(self, experiment_id, gender, has_license, proficiency, age, user_agent_simple, user_agent_full):
        self.experiment_id = experiment_id
        self.gender = gender
        self.has_license = has_license
        self.proficiency = proficiency
        self.age = int(age)
        self.user_agent_simple = user_agent_simple
        self.user_agent_full = user_agent_full
        self.labels = ["saopaulover-1min-s-yaw0", "saopaulover-1min-s-yaw90", "saopaulover-1min-t-yaw0",
                        "saopaulover-1min-t-yaw90", "saopaulover-1min-yaw0", "saopaulover-1min-yaw90"]
        self.videos = [0, 0, 0, 0, 0, 0]
        self.selections = []

    def add_prefer_count(self, first_variant, second_variant, preferred):
        if preferred == '1':
            selected = second_variant
            contender = first_variant
        else:
            selected = first_variant
            contender = second_variant
        """
        preferred_index = self.labels.index(selected)
        self.videos[preferred_index] += 1
        """
        self.selections.append({"selected": selected,
                                "contender": contender
                                })

    def get_selected_count(self):
        selected_dict = {"saopaulover-1min-s-yaw0": 0, "saopaulover-1min-s-yaw90": 0, "saopaulover-1min-t-yaw0": 0,
                         "saopaulover-1min-t-yaw90": 0, "saopaulover-1min-yaw0": 0, "saopaulover-1min-yaw90": 0}
        for selection in self.selections:
            selected_dict[selection["selected"]] += 1

        return selected_dict

    def get_selected_quality_count(self, include_same_match=True, is_percent=False):
        starting_point = -1
        if include_same_match:
            starting_point = 0
        selected_dict = {"Terrible": starting_point, "Middle": starting_point, "Great": starting_point}
        for selection in self.selections:
            selected = selection["selected"]
            if selected == "saopaulover-1min-t-yaw90" or selected == "saopaulover-1min-t-yaw0":
                selected_dict["Terrible"] += 1
            elif selected == "saopaulover-1min-s-yaw90" or selected == "saopaulover-1min-s-yaw0":
                selected_dict["Middle"] += 1
            else:
                selected_dict["Great"] += 1

        if is_percent:
            selected_dict = self.turn_into_percent(selected_dict)

        return selected_dict

    def get_hq_lq(self):
        selected_dict = {"HQ": 0, "LQ": 0}
        for selection in self.selections:
            selected = selection["selected"]
            contender = selection["contender"]
            quality_s = selected[17]
            quality_c = contender[17]
            if quality_c == quality_s:
                continue
            if quality_s == 'y':
                selected_dict["HQ"] += 1
            elif quality_s == 's' and quality_c == 't':
                selected_dict["HQ"] += 1
            else:
                selected_dict["LQ"] += 1
        return selected_dict

    @staticmethod
    def turn_into_percent(selected_dict: dict):
        total_value = 0
        for value in selected_dict.values():
            total_value += value
        for key in selected_dict:
            selected_dict[key] /= total_value

        return selected_dict
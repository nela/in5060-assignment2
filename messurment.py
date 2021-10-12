

class Candidate:
    def __init__(self, experiment_id, gender, has_license, proficiency, age, user_agent_simple, user_agent_full):
        self.experiment_id = experiment_id
        self.gender = gender
        self.has_license = has_license
        self.proficiency = proficiency
        self.age = age
        self.user_agent_simple = user_agent_simple
        self.user_agent_full = user_agent_full
        self.labels = ["saopaulover-1min-s-yaw0", "saopaulover-1min-s-yaw90", "saopaulover-1min-t-yaw0",
                        "saopaulover-1min-t-yaw90", "saopaulover-1min-yaw0", "saopaulover-1min-yaw90"]
        self.videos = [0, 0, 0, 0, 0, 0]
        self.selections = []

    def add_prefer_count(self, first_variant, second_variant, preferred):
        if preferred == 1:
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


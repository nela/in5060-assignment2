import csv
from messurment import Candidate


def read_candidates():
    candidates = []
    with open("data/log.csv", "r") as file:
        next(file) # header
        count = 0
        c = None
        reader = csv.reader(file)
        for row in reader:
            if count == 0:
                age = row[1]
                gender = row[2]
                drivers_license = row[3]
                user_agent_simple = row[4]
                user_agent_full = row[5]
                proficiency = row[6]
                experiment_id = row[7]
                timestamp = row[8]
                firstv = row[9]
                secondv = row[10]
                selected = row[11]

                c = Candidate(experiment_id, gender, drivers_license, proficiency,
                    age, user_agent_simple, user_agent_full)
                c.add_prefer_count(firstv, secondv, selected)

                count += 1
            elif count < 14:
                count += 1
                c.add_prefer_count(row[9], row[10], row[11])
            elif count == 14:
                c.add_prefer_count(row[9], row[10], row[11])
                candidates.append(c)
                count = 0
            else:
                print('undefined')

    return candidates

# cands = read_candidates()
#
# ids = []
# for c in read_candidates():
#     print(c.experiment_id)
#     ids.append(c.experiment_id)
#
# print(len(set(ids)))


# def read_generic():
#     with open("data/log.csv", "r") as file:
#         next(file)
#         reader = csv.reader(file)
#         count = 0
#         samples = []
#         for row in reader:
#             if count == 0:
#                 test = dict(
#                     age = row[1],
#                     gender = row[2],
#                     drivers_licence = row[3],
#                     user_agent_simple = row[4],
#                     user_agent_full = row[5],
#                     proficiency = row[6],
#                     experiment_id = row[7],
#                     timestamp = row[8],
#                     samples = [row[9], row[10]]
#                     selected_sample = row[9] if row[11] == 1 else row[10]
#                 )
#             elif count < 14:
#
#
#
#

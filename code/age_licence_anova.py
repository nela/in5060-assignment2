from messurment import Candidate
from read_file import read_candidates

from typing import List

candidates = read_candidates()

# print(len(candidates))
# for c in candidates:
#     print(c.experiment_id)

under25_license, column_mean = {
    "saopaulover-1min-s-yaw0": 0,
    "saopaulover-1min-s-yaw90": 0,
    "saopaulover-1min-t-yaw0": 0,
    "saopaulover-1min-t-yaw90": 0,
    "saopaulover-1min-yaw0": 0,
    "saopaulover-1min-yaw90": 0
}

under_license: List[Candidate] = []
under_nolicense = []
under_undefined = []
over_license = []
over_nolicense = []
over_undefined = []
age_undefined = []

for c in candidates:
    if int(c.age) <= 25 and c.has_license == "yes":
        under_license.append(c)
    elif int(c.age) <= 25 and c.has_license == "no":
        under_nolicense.append(c)
    elif int(c.age) <= 25:
        under_undefined.append(c)
    elif int(c.age) > 25 and c.has_license == "yes":
        over_license.append(c)
    elif int(c.age) > 25 and c.has_license == "no":
        over_nolicense.append(c)
    elif int(c.age) > 25:
        over_undefined.append(c)
    else:
        age_undefined.append(c)

measurements = [
    under_license,
    under_nolicense,
    under_undefined,
    over_license,
    over_nolicense,
    over_undefined,
    age_undefined
]

for c in under_license:
    print(c.get_selected_count())

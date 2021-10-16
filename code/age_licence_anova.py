from messurment import Candidate
from read_file import read_candidates

from typing import List

candidates: List[Candidate] = read_candidates()


def get_gendered(candidates):
    males, females, other = [], [], []
    for c in candidates:
        if c.gender == "male":
            males.append(c)
        elif c.gender == "female":
            females.append(c)
        elif c.gender == "other":
            other.append(c)

    return males, females, other


def get_hq_lq_count(candidates: List[Candidate]):
    hq_choice, lq_choice, side, back = 0, 0, 0, 0
    for c in candidates:
        for s in c.selections:
            if '-t-' in s["selected"]:
                if '-t-' not in s["contender"]:
                    lq_choice += 1
                elif 'yaw90' in s["selected"]:
                    side += 1
                else:
                    back += 1
            elif '-s-' in s["selected"]:
                if '-t-' in s["contender"]:
                    hq_choice += 1
                elif '-t-' not in s["contender"] and '-s-' not in s["contender"]:
                    lq_choice += 1
                elif 'yaw90' in s["selected"]:
                    side += 1
                else:
                    back += 1
            else:
                if '-t-' not in s["contender"] and '-s-' not in s["contender"]:
                    hq_choice += 1
                elif 'yaw90' in s["selected"]:
                    side += 1
                else:
                    back += 1

    return { "hq_choice" : hq_choice, "lq_choice" : lq_choice, "side" : side, "back" : back }


def get_age_and_license(candidates: List[Candidate]):
    under25_license: List[Candidate] = []
    under25_nolicense: List[Candidate] = []
    under25_undefined: List[Candidate] = []
    over25_license: List[Candidate] = []
    over25_nolicense: List[Candidate] = []
    over25_undefined: List[Candidate] = []
    age_undefined: List[Candidate] = []

    for c in candidates:
        if int(c.age) <= 25 and c.has_license == "yes":
            under25_license.append(c)
        elif int(c.age) <= 25 and c.has_license == "no":
            under25_nolicense.append(c)
        elif int(c.age) <= 25:
            under25_undefined.append(c)
        elif int(c.age) > 25 and c.has_license == "yes":
            over25_license.append(c)
        elif int(c.age) > 25 and c.has_license == "no":
            over25_nolicense.append(c)
        elif int(c.age) > 25:
            over25_undefined.append(c)
        else:
            age_undefined.append(c)

    return { "under25_license" : under25_license,
            "under25_nolicense" : under25_nolicense,
            "under25_undefined" : under25_undefined,
            "over25_license" : over25_license,
            "over25_nolicense" : over25_nolicense,
            "over25_undefined" : over25_undefined,
            "age_undefined" : age_undefined }

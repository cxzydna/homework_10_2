# Importing a library to work with a json file
import json


def load_candidates():
    """
    The function converts the json format to a dictionary
    :return:    - a dictionary of candidates

    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_all(candidates):
    """
    The function returns the full list of candidates
    :param candidates:   - a list of candidates
    :return:             - a list of candidates

    """
    return candidates


def get_by_pk(pk, candidates):
    """
    The function returns the candidate by his position
    :param pk:          - the position of the candidate
    :param candidates:  - a list of candidates
    :return:            - candidate

    """
    return candidates[pk - 1]


def get_by_skill(skill_name, candidates):
    """
    The function returns the candidate by his skills
    :param skill_name:  - the required skill
    :param candidates:  - a list of candidates
    :return:            - candidate

    """
    result = []
    for i in candidates:
        skills = i["skills"].lower().split(", ")
        if skill_name.strip().lower() in skills:
            result.append(i)
    return result

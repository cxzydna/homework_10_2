import json


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_all(candidates):
    return candidates


def get_by_pk(pk, candidates):
    return candidates[pk - 1]


def get_by_skill(skill_name, candidates):
    result = []
    for i in candidates:
        skills = i["skills"].lower().split(", ")
        if skill_name.strip().lower() in skills:
            result.append(i)
    return result


print(get_by_skill('python', load_candidates()))
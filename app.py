from utils import get_all, load_candidates, get_by_pk, get_by_skill
from flask import Flask

data = load_candidates()

app = Flask(__name__)


@app.route('/')
def main_page():
    candidates = get_all(data)
    result = ''
    for i in candidates:
        a = f'<pre>Имя кандидата - {i["name"]}\n' \
            f'Позиция кандидата - {i["pk"]}\n' \
            f'Навыки кандидата - {i["skills"]}\n</pre>'
        result += a
    return result


@app.route('/candidates/<int:uid>')
def candidate_page(uid):
    candidate = get_by_pk(uid, data)
    url = candidate["picture"]
    result = f'<img src="{url}"\n' \
             f'<pre>Имя кандидата - {candidate["name"]}.\n' \
             f'Позиция кандидата - {candidate["pk"]}.\n' \
             f'Навыки кандидата - {candidate["skills"]}.</pre>'
    return result


@app.route('/skills/<skill>')
def candidates_by_skill_page(skill):
    candidates = get_by_skill(skill, data)
    result = ''
    for candidate in candidates:
        list_of_candidates = f'<pre>Имя кандидата - {candidate["name"]}\n' \
                 f'Позиция кандидата - {candidate["pk"]}\n' \
                 f'Навыки кандидата - {candidate["skills"]}</pre>'
        result += list_of_candidates
    return result


if __name__ == '__main__':
    app.run()

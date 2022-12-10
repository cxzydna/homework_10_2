# Importing the flask
from flask import Flask

# Importing the necessary functions for the program to work
from utils import get_all, load_candidates, get_by_pk, get_by_skill

data = load_candidates()

app = Flask(__name__)


@app.route('/')
def main_page():
    candidates = get_all(data)
    result = ''
    for i in candidates:
        a = f'<pre>Имя кандидата - {i["name"]}<br>' \
            f'Позиция кандидата - {i["pk"]}<br>' \
            f'Навыки кандидата - {i["skills"]}<br></pre>'
        result += a
    return result


@app.route('/candidates/<int:uid>')
def candidate_page(uid):
    candidate = get_by_pk(uid, data)
    url = candidate["picture"]
    result = f'<br>' \
             f'<img src="{url}"<br>' \
             f'<pre>Имя кандидата - {candidate["name"]}<br>' \
             f'Позиция кандидата - {candidate["pk"]}<br>' \
             f'Навыки кандидата - {candidate["skills"]}<br></pre>'

    return result


@app.route('/skills/<skill>')
def candidates_by_skill_page(skill):
    candidates = get_by_skill(skill, data)
    result = ''
    for candidate in candidates:
        list_of_candidates = f'<pre>Имя кандидата - {candidate["name"]}<br>' \
                 f'Позиция кандидата - {candidate["pk"]}<br>' \
                 f'Навыки кандидата - {candidate["skills"]}<br></pre>'
        result += list_of_candidates
    return result


if __name__ == '__main__':
    app.run()

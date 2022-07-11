from flask import Flask

app = Flask(__name__)

@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    """Поиск кандидата по id"""
    candidate: dict = get_candidate_by_id(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result

@app.route('/skills/<str:uid>')
def page_skills(uid):
    """Поиск по навыку"""
    skill_lower = skill.lower()
    candidates: list[dict] = get_candidate_by_skill(skill)
    result = format_candidates(candidates)
    return result

app.run()


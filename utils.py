import json

for candidate in candidates:
    result += f"""
        {candidate["name"]}\n
        {candidate["position"]}\n
        {candidate["skills"]}\n
    """

def get_all_candidates() -> list[dict]:
    return load_json()

def get_candidate_by_id(uid: int) -> dict | None:
    candidates = get_all_candidates()
    for candidates in candidates:
        if candidate['id'] == uid:
            return candidate
    return None

def get_candidate_by_skill(skill: str) -> list[dict]:
    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].split(','):
            result.append(candidate)
    return result
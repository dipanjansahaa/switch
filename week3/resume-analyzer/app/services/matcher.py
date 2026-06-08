import json

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def skill_match_score(
    resume_skills,
    jd_skills
):
    resume_set = {
        skill.lower()
        for skill in resume_skills
    }

    jd_set = {
        skill.lower()
        for skill in jd_skills
    }

    matched = resume_set & jd_set

    missing = jd_set - resume_set

    score = (
        len(matched)
        / len(jd_set)
        * 100
    ) if jd_set else 0

    return {
        "score": round(score, 2),
        "matched_skills": list(matched),
        "missing_skills": list(missing)
    }

def compare_resume_and_jd(
    resume_data,
    jd_data
):

    skill_analysis = skill_match_score(
        resume_data["skills"],
        jd_data["required_skills"]
    )

    match_data = {
        "candidate_name":
            resume_data["candidate_name"],

        "match_score":
            skill_analysis["score"],

        "matched_skills":
            skill_analysis["matched_skills"],

        "missing_skills":
            skill_analysis["missing_skills"]
    }

    with open(
        "outputs/match_data.json",
        "w"
    ) as f:
        json.dump(
            match_data,
            f,
            indent=4
        )

    return match_data

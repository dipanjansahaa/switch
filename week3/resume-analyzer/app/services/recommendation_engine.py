import json

from app.services.ollama_client import generate_response
from app.prompts.recommendation_prompt import (
    RECOMMENDATION_PROMPT
)

from app.utils.json_utils import clean_json


def generate_recommendations(
    resume_data,
    jd_data,
    match_results
):
    prompt = f"""
{RECOMMENDATION_PROMPT}

Resume Data:
{json.dumps(resume_data, indent=2)}

Job Description Data:
{json.dumps(jd_data, indent=2)}

Match Results:
{json.dumps(match_results, indent=2)}
"""

    response = generate_response(prompt)

    response = clean_json(response)

    recommendation_data = json.loads(response)

    with open(
        "outputs/recommendation_data.json",
        "w"
    ) as f:
        json.dump(
            recommendation_data,
            f,
            indent=4
        )

    return recommendation_data
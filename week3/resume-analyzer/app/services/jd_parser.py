import json

from app.prompts.jd_prompt import (
    JD_EXTRACTION_PROMPT
)

from app.services.ollama_client import (
    generate_response
)

from app.models.schemas import (
    JobDescriptionData
)

from app.utils.json_utils import (
    clean_json
)


def parse_job_description(
    jd_text: str
) -> JobDescriptionData:

    prompt = f"""
{JD_EXTRACTION_PROMPT}

Job Description:

{jd_text}
"""

    result = generate_response(prompt)

    result = clean_json(result)

    data = json.loads(result)

    jd_data = JobDescriptionData.model_validate(
        data
    )

    with open(
        "outputs/jd_data.json",
        "w"
    ) as f:
        json.dump(
            jd_data.model_dump(),
            f,
            indent=4
        )

    return jd_data
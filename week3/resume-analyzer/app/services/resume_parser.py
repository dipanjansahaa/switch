import json

from app.prompts.resume_prompt import (
    RESUME_EXTRACTION_PROMPT
)

from app.services.ollama_client import (
    generate_response
)

from app.models.schemas import ResumeData

from app.utils.json_utils import clean_json

def parse_resume(resume_text: str) -> ResumeData:

    prompt = f"""
{RESUME_EXTRACTION_PROMPT}

Resume:

{resume_text}
"""

    result = generate_response(prompt)

    result = clean_json(result)

    data = json.loads(result)

    resume_data = ResumeData.model_validate(
        data
    )

    with open(
        "outputs/resume_data.json",
        "w"
    ) as f:
        json.dump(
            resume_data.model_dump(),
            f,
            indent=4
        )

    return resume_data
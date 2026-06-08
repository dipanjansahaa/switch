'''from app.utils.pdf_reader import extract_text_from_pdf

pdf_path = "uploads/CV.pdf"

resume_text = extract_text_from_pdf(pdf_path)

print(resume_text)'''

'''from app.utils.pdf_reader import (
    extract_text_from_pdf
)

from app.services.resume_parser import (
    parse_resume
)

resume_text = extract_text_from_pdf(
    "uploads/CV.pdf"
)

resume_data = parse_resume(
    resume_text
)

print(resume_data)

from app.services.jd_parser import (
    parse_job_description
)

with open(
    "uploads/job_description.txt",
    "r",
    encoding="utf-8"
) as f:
    jd_text = f.read()

jd_data = parse_job_description(
    jd_text
)

print(jd_data)'''

'''from app.services.matcher import (
    load_json,
    compare_resume_and_jd
)

resume = load_json(
    "outputs/resume_data.json"
)

jd = load_json(
    "outputs/jd_data.json"
)

result = compare_resume_and_jd(
    resume,
    jd
)

print(result)'''

from app.services.matcher import (
    load_json,
    compare_resume_and_jd
)

from app.services.recommendation_engine import (
    generate_recommendations
)

resume_data = load_json(
    "outputs/resume_data.json"
)

jd_data = load_json(
    "outputs/jd_data.json"
)

match_results = compare_resume_and_jd(
    resume_data,
    jd_data
)

recommendations = generate_recommendations(
    resume_data,
    jd_data,
    match_results
)

print(recommendations)
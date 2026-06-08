import json

from app.utils.pdf_reader import extract_text_from_pdf

from app.services.resume_parser import parse_resume
from app.services.jd_parser import parse_job_description

from app.services.matcher import compare_resume_and_jd
from app.services.recommendation_engine import generate_recommendations


def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def main():

    print("Reading Resume...")

    resume_text = extract_text_from_pdf(
        "uploads/CV.pdf"
    )

    resume_data = parse_resume(
        resume_text
    )

    save_json(
        resume_data.model_dump(),
        "outputs/resume_data.json"
    )

    print("Resume Parsed")


    print("Reading Job Description...")

    with open(
        "uploads/job_description.txt",
        "r",
        encoding="utf-8"
    ) as f:

        jd_text = f.read()

    jd_data = parse_job_description(
        jd_text
    )

    save_json(
        jd_data.model_dump(),
        "outputs/jd_data.json"
    )

    print("JD Parsed")


    print("Matching Resume and JD...")

    match_data = compare_resume_and_jd(
        resume_data.model_dump(),
        jd_data.model_dump()
    )

    save_json(
        match_data,
        "outputs/match_data.json"
    )

    print("Matching Complete")


    print("Generating Recommendations...")

    recommendations = generate_recommendations(
        resume_data.model_dump(),
        jd_data.model_dump(),
        match_data
    )

    save_json(
        recommendations,
        "outputs/recommendation_data.json"
    )

    print("Recommendations Generated")


    print("\nDone!\n")

    print(
        json.dumps(
            recommendations,
            indent=4
        )
    )


if __name__ == "__main__":
    main()
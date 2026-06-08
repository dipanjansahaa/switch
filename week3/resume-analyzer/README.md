# AI Resume Analyzer

An AI-powered Resume Analyzer built with Python and Ollama using the Llama 3.2 model.

The application extracts structured information from resumes and job descriptions, compares candidate skills with job requirements, calculates a match score, and generates ATS-style recommendations.

## Features

* Extract text from PDF resumes
* Parse candidate information using LLMs
* Extract skills, education, projects, and experience
* Analyze job descriptions
* Compare resume skills with job requirements
* Calculate match scores
* Identify missing skills
* Generate ATS-style recommendations
* Save all outputs in structured JSON format

---

## Tech Stack

* Python
* Ollama
* Llama 3.2
* Pydantic
* PyPDF

---

## Project Structure

```text
resume-analyzer/

├── app/
│   ├── models/
│   │   └── schemas.py
│   │
│   ├── prompts/
│   │   ├── resume_prompt.py
│   │   ├── jd_prompt.py
│   │   └── recommendation_prompt.py
│   │
│   ├── services/
│   │   ├── ollama_client.py
│   │   ├── resume_parser.py
│   │   ├── jd_parser.py
│   │   ├── matcher.py
│   │   └── recommendation_engine.py
│   │
│   └── utils/
│       ├── pdf_reader.py
│       └── json_utils.py
│
├── uploads/
│   ├── CV.pdf
│   └── job_description.txt
│
├── outputs/
│   ├── resume_data.json
│   ├── jd_data.json
│   ├── match_results.json
│   └── recommendation_data.json
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd resume-analyzer
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Ollama Setup

Pull the model:

```bash
ollama pull llama3.2:3b
```

Verify installation:

```bash
ollama list
```

---

## Usage

Place your files inside the `uploads` folder:

```text
uploads/
├── CV.pdf
└── job_description.txt
```

Run the application:

```bash
python main.py
```

Generated outputs will be saved in:

```text
outputs/
├── resume_data.json
├── jd_data.json
├── match_results.json
└── recommendation_data.json
```

---

## Workflow

```text
Resume PDF
    │
    ▼
PDF Text Extraction
    │
    ▼
Resume Parsing (LLM)
    │
    ▼
Structured Resume Data

Job Description
    │
    ▼
JD Parsing (LLM)
    │
    ▼
Structured JD Data

Resume Data + JD Data
    │
    ▼
Skill Matching
    │
    ▼
Match Score & Missing Skills
    │
    ▼
ATS Recommendations
```

---

## Example Output

### Match Result

```json
{
    "candidate_name": "John Doe",
    "match_score": 75.0,
    "matched_skills": [
        "python",
        "fastapi"
    ],
    "missing_skills": [
        "docker",
        "aws"
    ]
}
```

### Recommendations

```json
{
    "strengths": [
        "Strong Python skills"
    ],
    "weaknesses": [
        "Missing cloud experience"
    ],
    "recommendations": [
        "Add Docker projects",
        "Learn AWS fundamentals"
    ]
}
```

---

## Learning Outcomes

This project demonstrates:

* Prompt Engineering
* Structured Outputs
* Local LLM Integration
* Ollama Usage
* JSON Processing
* PDF Processing
* Pydantic Validation
* Information Extraction
* ATS Analysis
* LLM + Traditional Logic Hybrid Systems


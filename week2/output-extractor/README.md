# JSON Output Extractor

A Python-based AI-powered information extraction tool that extracts structured details from PDF and TXT files using Ollama and local LLMs.

The project can be used to extract information from resumes (CVs), documents, and text files and generate structured JSON output.

---

## Features

* Extract text from PDF files
* Process plain text files
* Extract structured information using local LLMs
* Generate JSON output
* Experiment with multiple Ollama models
* Runs completely locally

---

## Tech Stack

* Python
* Ollama
* Llama 3.2
* Gemma (tested)
* dotenv
* PyMuPDF / PDF processing libraries

---

## Project Structure

output-extractor/

├── app.py
├── app2.py
├── test.py
├── CV.pdf
├── sample.txt
├── requirements.txt
├── README.md
└── outputs/
    ├── result.json
    └── result2.json

---

## Files

### app.py

Contains reusable functions for:

* PDF text extraction
* Text processing
* Prompt generation
* LLM interaction
* JSON formatting

### app2.py

Main execution file that:

* Loads input files
* Calls extraction functions
* Tests different Ollama models
* Generates structured JSON output

---

## Example Use Cases

* Resume/CV information extraction
* Candidate profile generation
* Document data extraction
* Converting unstructured text into JSON

---

## Input

Supported inputs:

* PDF files (.pdf)
* Text files (.txt)

Example:

* CV.pdf
* sample.txt

---

## Output

Structured JSON files generated inside the outputs folder.

Example:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "skills": [
    "Python",
    "FastAPI",
    "Machine Learning"
  ]
}
```

---

## Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Ollama:

```bash
ollama serve
```

Run the application:

```bash
python app2.py
```

---

## Learning Objectives

This project was built to practice:

* Prompt Engineering
* Local LLM Integration
* Information Extraction
* JSON Structured Outputs
* Working with Ollama Models
* Python Project Organization

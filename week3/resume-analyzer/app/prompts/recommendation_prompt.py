RECOMMENDATION_PROMPT = """
You are an ATS expert.

Given:

1. Resume Data
2. Job Description Data
3. Match Results

Provide:

{
    "strengths": [],
    "weaknesses": [],
    "recommendations": []
}

Return ONLY JSON.
"""
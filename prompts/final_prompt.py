from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

final_prompt = PromptTemplate(
    template="""
You are an expert interview coach.

Generate an improved interview answer for the candidate.

Question:
{question}

Candidate's Original Answer:
{answer}

Evaluation:
{evaluation}

Feedback:
{feedback}

Candidate Profile:
Role: {role}
Experience: {experience}
Technology: {technology}

Generate:

1. Improved Sample Answer
   - Technically correct
   - Appropriate for the candidate's experience
   - Interview-ready
   - Well structured

2. Key Concepts To Revise

3. Personalized Preparation Recommendations

4. Possible Follow-up Interview Questions

Focus on practical improvement.
""",
    input_variables=[
        "question",
        "answer",
        "evaluation",
        "feedback",
        "role",
        "experience",
        "technology",
    ],
)

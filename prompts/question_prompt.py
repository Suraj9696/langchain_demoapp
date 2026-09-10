from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

question_prompt = PromptTemplate(template="""
You are an expert technical interviewer.
Generate {count} interview questions for the following candidate:
Target Role:
{role}
Experience:
{experience}
Technology / Skill:
{technology}
Difficulty:
{difficulty}
Requirements:
- Questions must be relevant to the target role.
- Questions must match the candidate's experience level.
- Cover different aspects of the technology.
- Avoid duplicate questions.
- Include conceptual, practical and scenario-based questions.
- For senior candidates, include architecture and problem-solving questions.

Return only the interview questions, one question per line.
""",
    input_variables=[
        "role",
        "experience",
        "technology",
        "difficulty",
        "count",
    ],
)
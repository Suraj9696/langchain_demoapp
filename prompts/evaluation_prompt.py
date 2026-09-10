from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

evaluation_prompt = PromptTemplate(template="""
You are a senior technical interviewer.

Evaluate the candidate's answer.

INTERVIEW QUESTION:
{question}

CANDIDATE ANSWER:
{answer}

CANDIDATE PROFILE:
Role: {role}
Experience: {experience}
Technology: {technology}
Difficulty: {difficulty}

Evaluate using these dimensions:

1. Correctness
   - Are the technical statements correct?
   - Are there misconceptions?

2. Completeness
   - Did the candidate address important aspects?

3. Clarity
   - Is the explanation structured and easy to understand?

4. Technical Depth
   - Does the answer demonstrate appropriate depth for the
     candidate's experience?

Scoring:
90-100 = Excellent
75-89  = Strong
50-74  = Partially Correct
0-49   = Weak

Classification must be one of:
strong
partially_correct
weak

Identify:
- strengths
- improvement areas
- missing concepts
- overall feedback

Return the result using the required structured format.
""",
    input_variables=[
        "question",
        "answer",
        "role",
        "experience",
        "technology",
        "difficulty",
    ],
)

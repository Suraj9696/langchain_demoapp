from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

strong_prompt = PromptTemplate(template="""
The candidate gave a strong answer.

Question:
{question}

Candidate Answer:
{answer}

Evaluation:
{evaluation}

Provide encouraging interview-coach feedback.
Focus on:
- What made the answer strong
- What could make it even better
- What an experienced interviewer may ask next
""",
    input_variables=["question", "answer", "evaluation"],
)


partial_prompt = PromptTemplate(template="""
The candidate gave a partially correct answer.

Question:
{question}

Candidate Answer:
{answer}

Evaluation:
{evaluation}

Explain:
- What the candidate got right
- What is missing
- What should be corrected
- What concepts should be revised
""",
    input_variables=["question", "answer", "evaluation"],
)


weak_prompt = PromptTemplate(template="""
The candidate gave a weak answer.

Question:
{question}

Candidate Answer:
{answer}

Evaluation:
{evaluation}

Provide constructive feedback.
Explain:
- Fundamental misunderstanding
- Important missing concepts
- What the candidate should learn
- How to structure the answer next time
""",
    input_variables=["question", "answer", "evaluation"],
)

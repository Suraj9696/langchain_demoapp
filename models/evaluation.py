from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

class EvaluationResult(BaseModel):
    correctness: int = Field(description="Correctness score from 0 to 100")
    completeness: int = Field(description="Completeness score from 0 to 100")
    clarity: int = Field(description="Clarity score from 0 to 100")
    technical_depth: int = Field(
        description="Technical depth score from 0 to 100"
    )
    overall_score: int = Field(
        description="Overall score from 0 to 100"
    )
    classification: Literal[
        "strong",
        "partially_correct",
        "weak"
    ]
    strengths: list[str]
    improvement_areas: list[str]
    missing_concepts: list[str]
    evaluator_feedback: str

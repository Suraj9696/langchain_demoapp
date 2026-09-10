from langchain_google_genai import ChatGoogleGenerativeAI
from models.evaluation import EvaluationResult
from prompts.evaluation_prompt import evaluation_prompt
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

evaluator_llm = llm.with_structured_output(EvaluationResult)

evaluation_chain = evaluation_prompt | evaluator_llm

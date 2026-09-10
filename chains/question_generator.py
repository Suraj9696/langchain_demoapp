from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from prompts.question_prompt import question_prompt
from dotenv import load_dotenv

load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

question_chain = question_prompt | llm | StrOutputParser()

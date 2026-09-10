from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch

from prompts.feedback_prompts import (
    strong_prompt,
    partial_prompt,
    weak_prompt,
)
from dotenv import load_dotenv

load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

strong_chain = strong_prompt | llm | StrOutputParser()
partial_chain = partial_prompt | llm | StrOutputParser()
weak_chain = weak_prompt | llm | StrOutputParser()


feedback_branch = RunnableBranch(
    (
        lambda x: x["evaluation"].classification == "strong",
        strong_chain,
    ),
    (
        lambda x: x["evaluation"].classification == "partially_correct",
        partial_chain,
    ),
    weak_chain,
)

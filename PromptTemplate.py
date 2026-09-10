from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)

template = PromptTemplate(
    template="Write an article on the topic of {topic}", input_variables=["topic"])
template2 = PromptTemplate(
    template="Create 5 MCQ type questions with answers for the below article \n {article}"
)

# prompt = HumanMessage(content=template.invoke({"topic": 'AI'})) #Not the part of this use case

# prompt1 = template.invoke({"topic": "AI"})
# prompt2 = template.invoke({"topic": "Cyber Security"})

# response = llm.invoke(prompt1)

# print(response.text)

chain = template | llm | StrOutputParser() | template2 | llm | StrOutputParser()

print(chain.invoke({'topic': 'AI'}))
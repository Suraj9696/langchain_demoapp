from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)

conversation_history = [
    SystemMessage(content="You are a helful AI assistant who respond to queries with a bit of humour. You are using emojis to make your responses looks good. You only answer technical queries related to programming languages. Do not respond to any other questions other than programming languages. Keep your tone polite and professional")
]

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    conversation_history.append(HumanMessage(content=user_input))
    response = ''
    for chunk in llm.stream(conversation_history):
        response = response + chunk.text
        print(chunk.text, end="", flush=True)
    conversation_history.append(AIMessage(content=response))
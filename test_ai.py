from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


template = """ 
Answer the question below,

here is the conversation history: {context}

question: {question}

Answer:
"""
model = OllamaLLM(model="llama3")
promt = ChatPromptTemplate.from_template(template)
chain = promt | model

def handle_conversation():
    context = ""
    print("Welcome to the AI Chat Bot")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context":context, "question":user_input})
        print("Bot: ",result)
        context += f"\nUser: {user_input}\nAI: {result}"



if __name__ == "__main__":
    handle_conversation()

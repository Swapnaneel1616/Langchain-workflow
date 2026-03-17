import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI , OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate , PromptTemplate
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
import streamlit as st

load_dotenv()

model = ChatOpenAI()

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI , OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate , PromptTemplate
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
import streamlit as st


load_dotenv()


chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)
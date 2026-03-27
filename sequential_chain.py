from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
import os
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = "Generate a detailed report on {topic}"
)

prompt2 = PromptTemplate(
    template="Generate a 5 pointer summary from the following text \n {text}"
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt1|model|parser|prompt2|model|parser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()


prompt = PromptTemplate(
    template = "Generate 5 interesting facts about {topic}"
)

model = ChatOpenAI()
 
parser = StrOutputParser()

chain = prompt|model|parser

result = chain.invoke({'topic':'cricket'})


print(result)



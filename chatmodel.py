from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import os 
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model='gpt-4', temperature=0 , max_completion_tokens=10)

results = model.invoke("What is the capital of India?")

print(results)

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
import os 
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model='gpt-4', temperature=0 , max_completion_tokens=10)

results = model.invoke("What is the capital of India?")

print(results)


#Embeddings 
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

embed_result = embedding.embed_query("delhi is the capital of India")
print(str(embed_result))


#Multiple Embeddings
documents  = [
    "Delhi is the capital of India",
    "kolkata is the capital of West Bengal",
    "Paris the capital of France"
]

embed_doc = embedding.embed_documents(documents)
print(str(embed_doc))



#Document Similarity
query = "What is the capital of France?"

query_embed = embedding.embed_query(query)


print(cosine_similarity([query_embed], embed_doc))

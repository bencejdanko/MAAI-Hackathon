from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS, Chroma
from langchain.document_loaders import PyMuPDFLoader
from langchain.chains import RetrievalQA

import os

huggingface_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
print(huggingface_token)

from langchain_huggingface import HuggingFaceEndpoint

llama_model = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    max_length=256,
    temperature=0.7,
    token=huggingface_token,
    task="text-generation"
)

from langchain_core.prompts import PromptTemplate
import pandas as pd


question = "Who won the FIFA World Cup in the year 1994? "

template = """Question: {question}

Answer: Let's think step by step.

Example Response:



"""

prompt = PromptTemplate.from_template(template)

llm_chain = prompt | llama_model

print(llm_chain.invoke({"question": question}))

#Embedding Model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma.from_texts(texts, embedding_model, persist_directory="chroma_db")
vector_store.embeddings
# Load the CSV file
csv_file_path = "/path/to/your/csvfile.csv"
df = pd.read_csv(csv_file_path)

# Combine the relevant columns into a single text for each row
texts = df.apply(lambda row: f"Savings: {row['Savings']}, Assets: {row['Assets']}, Investments: {row['Investments']}, Debts: {row['Debts']}, Fixed Income: {row['Fixed Income']}, Response: {row['response']}", axis=1).tolist()

# Create embeddings from the texts
vector_store = Chroma.from_texts(texts, embedding_model, persist_directory="chroma_db")

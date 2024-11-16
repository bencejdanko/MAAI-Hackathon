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


user_data = {
"savings": [
{
"Description": "savings",
"Amount": 1000.0
},
{
"Description": "checkings",
"Amount": 500.0
}
],
"assets": [
{
"Description": "car",
"Purchase Price": 2000.0,
"Current Value": 1500.0,
"Status": "Fully Owned"
}
],
"investments": [
{
"Category": "US Stock Market",
"Description": "S&P500",
"Amount": 1000.0,
"Growth Rate": 4.0,
"Dividend Yield": 1.0
}
],
"debts": [
{
"Description": "Credit card",
"Amount": 100.0,
"Interest Rate": 35.0,
"Minimum Payment": 35.0
}
],
"income": [
{
"Type": "Cash",
"Amount": 50000.0
}
],
"investment_knowledge": "None",
"investment_goal": "Generating stable income",
"income_source": "Unstable",
"investment_risk": "3"
}

question = "What is the capital of Paris?"

template = """

Question: {question}

Answer: Let's think step by step.

"""

prompt2 = """

Question: What is the capital of Paris?

Answer: Let's think step by step.

"""

prompt = PromptTemplate.from_template(template)

llm_chain = prompt | llama_model

# print(llm_chain.invoke({"question": question, "user_data": user_data}))

print(llm_chain.invoke(prompt2))

# #Embedding Model
# embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# vector_store = Chroma.from_texts(texts, embedding_model, persist_directory="chroma_db")
# vector_store.embeddings
# # Load the CSV file
# csv_file_path = "/path/to/your/csvfile.csv"
# df = pd.read_csv(csv_file_path)

# # Combine the relevant columns into a single text for each row
# texts = df.apply(lambda row: f"Savings: {row['Savings']}, Assets: {row['Assets']}, Investments: {row['Investments']}, Debts: {row['Debts']}, Fixed Income: {row['Fixed Income']}, Response: {row['response']}", axis=1).tolist()

# # Create embeddings from the texts
# vector_store = Chroma.from_texts(texts, embedding_model, persist_directory="chroma_db")

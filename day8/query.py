import chromadb
import ollama

file_name = "code_sample.txt"

with open(file_name, "r") as file:
    text = file.read()

chunks = []
chunk_size = 100
chunk_overlap = 20
step = chunk_size - chunk_overlap

for i in range(0, len(text), step):
    chunk = text[i:i+chunk_size]
    chunks.append(chunk)

# Create embeddings using Ollama
embeddings = []
for chunk in chunks:
    response = ollama.embed(
        model="nomic-embed-text",
        input=chunk
    )
    embeddings.append(response["embeddings"][0])

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="My_documents")

ids = []
for i in range(len(chunks)):
    ids.append(f"{file_name}_{i}")

collection.add(
    ids=ids,
    documents=chunks,
    embeddings=embeddings
)

# Query Phase
question = input("Ask a question...")

question_response = ollama.embed(
    model="nomic-embed-text",
    input=question
)

question_embedding = question_response["embeddings"][0]

results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3
)

retrieved_results = results["documents"][0]
retrieved_ids = results["ids"][0]

# Prompting
context = "\n".join(retrieved_results)

prompt = f'''
Answer the question using the context provided below.
Question : {question}
Context : {context}
Answer:
'''

# Connecting to Local Model
response = ollama.chat(
    model="llama3.2:3b",
    messages=[{
        "role": "user",
        "content": prompt
    }]
)

print(response["message"]["content"])
import chromadb
import ollama
from sentence_transformers import SentenceTransformer
import streamlit as st

@st.cache_resource 
def load_model():
    return SentenceTransformer("all-MiniLM-L6-V2")
model=load_model()
st.balloons()
st.title("Use me - Ragbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.subheader(''':blue[**⚙️Chat settings**]''')
    if st.button("clearchat 🗑️"):
            st.session_state.messages = []
            st.write("Chat cleared successfully")
    personalities ={
        "Friend" : "Give answer in a friendly tone. 2 lines only",
        "Kid" : " Answer like you are explaining to a 5 years kid.answer in 2 lines",
        "Teacher" : "Give ans like as a teacher in 2 lines only"
    }
    personality = st.selectbox("Select a personality",personalities.keys())
    uploaded_file = st.file_uploader("Upload a file")
    if uploaded_file:
        text = uploaded_file.read().decode("utf-8")
        with st.expander("preview"):
            st.text(text)

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
            ids.append(f"{uploaded_file.name}_{i}")

        collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings
        )

# Query Phase
question = st.chat_input("Ask a question...")
if question:
    if uploaded_file:
        with st.chat_message("user"):
            st.write(question)
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
        with st.chat_message("assistant"):
            st.write(response["message"]["content"])
        with st.expander("Source"):
            for i in range(3):
                st.warning(
                    f"Chunk{i + 1}\n\n"
                    f"ID: {retrieved_ids[i]}\n\n"
                    f"{retrieved_results[i]}"
                )
    else:
        with st.chat_message("user"):
                st.write(question)
        with st.spinner("Thinking..."):
                response = ollama.chat(
                    model = "llama3.2:3b",
                    messages = [
                        {"role":"system",
                         "content":personalities[personality]}
                    ]+ st.session_state.messages
                    )
        st.session_state.messages.append(
                    {"role":"assistant",
                    "content":response["message"]["content"]
                    }
                )
        
        with st.chat_message("assistant"):
                st.write(response["message"]["content"])
        
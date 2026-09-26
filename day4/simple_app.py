import streamlit as st 
import ollama
st.header("My first App!!!")
st.write("Welcome to my AI application!")
name = st.text_input( "Enter your name:")
if st.button("Submit"):
    st.write("Hello", name)



st.badge("My AI ChatBot")


st.latex("Welcome!   Ask   me   anything.")
if "messages" not in st.session_state:
    st.session_state.messages =[ ]
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
question = st.chat_input("Type your message...")
if question:
    st.session_state.messages.append({
        "role":"user",
        "content":question
    })
    with st.chat_message("user"):
        st.write(question)

        response =ollama.chat(
            model = "llama3.2:3b",
            messages =st.session_state.messages
        )

        answer = response["message"]["content"]

        st.session_state.messages.append({
            "role":"assistant",
            "content":answer
        })

        with st.chat_message("assistant"):
            st.write(answer)
            
            
st.badge("Success", icon=":material/check:", color="green")
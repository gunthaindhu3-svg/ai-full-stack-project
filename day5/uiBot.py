import ollama 
import streamlit as st 
st.title(''':blue[Welcome] :yellow[to my] :green[ChatBot App]:violet[!!!]''')
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
    uploaded_file=st.file_uploader("#Upload a text File..")
    try:
        if uploaded_file:
            context = uploaded_file.read().decode("utf-8")
            st.success("File uploaded successfully!")
            
            if st.button("display"):
                st.text(context)
    except :
        
        st.error("not a valid file")
       

if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Ask me anything🤔")
if question:
    st.session_state.messages.append(
            {"role" : "user",
            "content" : question}
        )
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

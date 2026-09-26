import streamlit as st 

st.header("This is an app!!!")
st.subheader(''':red[Welcome] :blue[to my] :violet[AI application!]''')
st.markdown("simple app")
name = st.text_input( "Enter your name:")

if st.button(''':blue["Submit"]'''):
    st.write("Hello", name)

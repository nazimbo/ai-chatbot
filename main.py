from openai import OpenAI
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("Clé API OpenAI", key="chatbot_api_key", type="password")
    "[Obtenir une clé OpenAI](https://platform.openai.com/account/api-keys)"

st.title("Charlie AI")
st.caption("Un chatbot utilisant l'API OpenAI.")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Comment puis-je vous aider ?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Entrez votre clé OpenAI pour continuer.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-4", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
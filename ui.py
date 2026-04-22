import streamlit as st
from agent import agent_response

st.set_page_config(page_title="AutoStream AI", page_icon="🎬")

st.title("🎬 AutoStream AI Agent")
st.markdown("### 🚀 Turn conversations into leads")

st.sidebar.title("About")
st.sidebar.info("AutoStream AI Agent\n\nConverts chats into leads using AI.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask about pricing or get started...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    response = agent_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)
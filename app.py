import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key
client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )




# configuring openai - api key
# working_dir = os.path.dirname(os.path.abspath(__file__))
# config_data = json.load(open(f"{working_dir}/config.json"))
# OPENAI_API_KEY = config_data["OPENAI_API_KEY"]
# openai.api_key = OPENAI_API_KEY

# configuring streamlit page settings
st.set_page_config(
    page_title="GPT-4o Chat",
    page_icon="💬",
    layout="centered"
)

# image_path01 = os.path.join('assets', r'C:\Users\chunt\OneDrive\Documents\[02] Job\Portfolio Streamlit\assets\ArtGravia-Vol-402-Kang-Inkyung-0001-0951116231.jpg')


link_url04 = "https://www.youtube.com/watch?v=PUd4-_91LnI"  # Replace with the desired clickable URL

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini-2024-07-18"

if "messages" not in st.session_state:
    st.session_state.messages = []
# Add a "Clear Chat" button to delete chat history
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
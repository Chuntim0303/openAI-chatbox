import os
import json
import streamlit as st
import openai # type: ignore

# configuring openai - api key
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
OPENAI_API_KEY = config_data["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

# configuring streamlit page settings
st.set_page_config(
    page_title="GPT-4o Chat",
    page_icon="💬",
    layout="centered"
)

# image_path01 = os.path.join('assets', r'C:\Users\chunt\OneDrive\Documents\[02] Job\Portfolio Streamlit\assets\ArtGravia-Vol-402-Kang-Inkyung-0001-0951116231.jpg')


link_url04 = "https://www.youtube.com/watch?v=PUd4-_91LnI"  # Replace with the desired clickable URL

# streamlit page title
st.sidebar.title("🤖 GPT-4o - ChatBot")
st.sidebar.link_button("Visit Github Repo", "https://streamlit.io/gallery")
if st.button("Clear Chat"):
    st.session_state.chat_history = []  # Clears chat history

tab1, tab2, tab3 = st.tabs(["Machine Learning Model", "Documentation", "Others"])

with tab1:
    # initialize chat session in streamlit if not already present
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    
    # List all available models


    # display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


    # input field for user's message
    user_prompt = st.chat_input("Ask GPT-4o...")

    if user_prompt:
        # add user's message to chat and display it
        st.chat_message("user").markdown(user_prompt)
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})

        # send user's message to GPT-4o and get a response
        response = openai.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                *st.session_state.chat_history
            ]
        )

        assistant_response = response.choices[0].message.content
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

        # display GPT-4o's response
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
        
        
        

with tab2:
    # Project Overview
    st.markdown("""
    <h3 style="color: #0CABA8;">Project Overview</h3>
    """, unsafe_allow_html=True)

    # Project Overview Description
    st.write("""
             This project involves building an interactive chatbox on Streamlit that uses the OpenAI API to generate real-time responses. 
             The application mimics a chatbot-like interface, leveraging the natural language processing (NLP) capabilities of OpenAI's GPT model.
             """)
    
    # OpenAI API
    st.markdown("""
    <h3 style="color: #0CABA8;">OpenAI API</h3>
    """, unsafe_allow_html=True)

    # OpenAI API Description
    st.write("""
            *OpenAI API* is a cloud-based platform that provides to access OpenAI's language models such as GPT-4, GPT-4o mini, and GPT-3.
            This project uses GPT-4o mini as it is much more cost effective compared to the GPT-4.
             """)















































# import streamlit as st
# import openai
# import os
# from openai import OpenAI

# # Set your OpenAI API key here
# openai.api_key = os.getenv("OPENAI_API_KEY")
# from openai import OpenAI
# client = OpenAI()

# response = client.completions.create(
#   model="gpt-3.5-turbo-instruct",
#   prompt="",
#   temperature=1,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )

# def main():
#     st.title("OpenAI Chatbot")

#     # Display user input text box
#     user_input = st.text_input("You:")

#     if st.button("Send"):
#         if user_input:
#             # Generate response
#             reply = response(user_input)
#             # Display user input and bot response
#             st.write(f"You: {user_input}")
#             st.write(f"Bot: {reply}")

# if __name__ == "__main__":
#     main()
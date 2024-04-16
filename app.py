from openai import OpenAI
import streamlit as st

# Read the API key and Setup an OpenAI Client
f = open("keys/.openai_api_key.txt")
key = f.read()
client = OpenAI(api_key=key)

######################
st.image("images/logo.png")
st.title("🤖 AI MCQ Generator")
st.subheader("My first Streamlit app 🈸")
######################

# Take User's input
prompt = st.text_input("Enter the topic : ")

# If the button is clicked, generate responses
if st.button("Generate") == True:
    response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": """You are a helpful AI Assistant.
                    
                                                    Given a Data Science topic you always generate 3 MCQ questions and answers for the test"""},
                    {"role": "user", "content": prompt}
                    ]
    )

    # Print the response on the web app
    st.write(response.choices[0].message.content)
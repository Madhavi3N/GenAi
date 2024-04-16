import streamlit as st
from openai import OpenAI


######################
st.snow()
st.image("images/img.png")
st.title("🤖 GenAI App - AI Code Reviewer")
######################

# Take User's input
prompt = st.text_area("Enter your Python code here:", height=200)

# The button is clicked to trigger the code review
if st.button("submit"):
    # Read the API key and Setup an OpenAI Client
    f = open("keys/.openai_api_key.txt")
    OPEN_API_KEY = f.read()
    client = OpenAI(api_key=OPEN_API_KEY)

    st.balloons()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": """
             You are a helpful AI Assistant. You take python code as an input from user.
             Your job is to explain the bugs nd generate the fixed code and display the output from the input.
             """},
                    {"role": "user", "content": f"Fix and explain the bugs in the following python code : {prompt}"}
        ],
        temperature=0.5
    )

    # Print the response on the web app
    review = response.choices[0].message.content

    st.subheader("Code Review")
    st.write(review)

    
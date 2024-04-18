import streamlit as st
import google.generativeai as genai


######################
st.snow()
st.image("images/img.png")
st.title('🚀 🤖 Gemini AI Chatbot 💬')
######################


# Reading the API Key and Configuring the API Key
f = open('keys/.gemini_api_key.txt')
key = f.read()
genai.configure(api_key=key)

# Initializing the gemini model
model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest',
                              system_instruction=""""Your Name is Innomanion AI, an AI Conversational Tutor in Data Science.
                              Innomatics Research Labs is a pioneer in “Transforming Career and Lives” of individuals in the Digital Space 
                              by catering advanced training on IBM Certified Data Science, Python, IBM Certified Predictive Analytics Modeler, 
                              Machine Learning, Artificial Intelligence (AI), Full-stack web development, Amazon Web Services (AWS), DevOps, Microsoft Azure, 
                              Big data Analytics, Digital Marketing, and Career Launching program for students who are willing to showcase their skills 
                              in the competitive job market with valuable credentials, and also can complete courses with a certificate.
                              """)


if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello, this is Innomanion AI, how I can help you today?"}
    ]


# Display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
# Receive user input
user_input = st.chat_input()

# Store user input in session
if user_input is not None:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
# Generate AI response and display
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        ai_response = model.generate_content(user_input)
        st.write(ai_response.text)
    new_ai_message = {"role": "assistant", "content": ai_response.text}
    st.session_state.messages.append(new_ai_message)
# Q&A Chatbot
#from langchain.llms import OpenAI
from dotenv import load_dotenv
import hmac
import streamlit as st 
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai

api_key =""
showhistory=""
st.set_page_config(page_title="Gemini Image Demo")
with st.sidebar:
# Show input for password.
    st.text_input( "Password", type="password", key="password")
    if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
        #api_key=st.text_input("Please provide your Gemini Pro API Key")
        genai.configure(api_key=st.secrets["api_key"])
        "[Get a Gemini API key](https://makersuite.google.com/app/apikey)"
    else:
        st.error("😕 Password incorrect")
        st.stop()
    showhistory = st.checkbox('Click to show history')

## function to load Gemini Pro model and get response
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

## Function to load OpenAI model and get respones

def get_gemini_response(input,image):
    
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app



st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)

#Import the libraries
import streamlit as st
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
import google.generativeai as genai
# from langchain_google_genai import ChatGoogleGenerativeAI

# Set page config
st.set_page_config(
    page_title="Code In Place - Final Project Ideas Generator",
    page_icon="🤖"
)

# Set the page title and caption
st.title("Code In Place - Final Project Ideas Generator")
st.caption("For when you need some inspiration!")

# Create tabs
tab1, tab2 = st.tabs(["Google Gemini","GPT3.5 Turbo (coming soon!)"])

#Code for Gemini
with tab1:
    # API Key Helptext
    st.write("""
    **Here's how you can get your own (FREE) Google Gemini API key:**
    1. Go to [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
    2. Sign in with your Google account
    3. Click on the "Create API Key" button.
    """)
    # API Key
    
    api_key = st.text_input("Google Gemini API Key (Remember to hit ENTER)", type="password")
    if not (api_key.startswith('AI')):
        st.warning('Please enter your API Key!', icon='⚠️')
    else:
        st.success('Success!', icon='✅')

    # Configure Gemini with the API Key
    genai.configure(api_key=api_key)

    # Setup the LLM
    topics = "Basic expressions, control flow, running basic console programs, lists, dictionaries, how to define a function, basic graphics."
    prompt = f"""Generate 10 ideas for a python project that can easily be accomplished by beginners who have just completed Stanford's Code in Place program. You can assume they have rudimentary knowledge of python {topics}"""
    config = {"temperature": 0.8}
    model = genai.GenerativeModel("gemini-pro",generation_config=config)
    
    st.write("""
             Don't worry! Your API key isn't saved anywhere.
             For extra security, you can revoke your API key once you're done.
             """)
    
    # Button to generate + response
    generate = st.button("Generate ideas", key="generate")
    if generate and prompt:
        response = model.generate_content(prompt)
        st.header("Here are your ideas:")
        st.info(response.text)

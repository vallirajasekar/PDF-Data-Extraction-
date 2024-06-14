import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_prompt)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template for querying PDF
query_prompt_template = """
You are an intelligent assistant with a deep understanding of various fields. Your task is to answer questions based on the content of a provided PDF document. Also Explain the Content Clearly in two or three lines 

PDF Content:
{text}

Question: {question}

Please provide a detailed and accurate answer.
"""

# Streamlit app
st.title("Smart PDF Query")
st.text("Upload a PDF and ask questions about its content")

# Text area for job description (JD) is removed as it's not needed for querying PDF
uploaded_file = st.file_uploader("Upload Your PDF", type="pdf", help="Please upload the PDF")

question = st.text_input("Enter your question about the PDF")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None and question:
        text = input_pdf_text(uploaded_file)
        input_prompt = query_prompt_template.format(text=text, question=question)
        response = get_gemini_response(input_prompt)
        st.subheader("Answer:")
        st.text(response)
    else:
        st.error("Please upload a PDF and enter a question.")

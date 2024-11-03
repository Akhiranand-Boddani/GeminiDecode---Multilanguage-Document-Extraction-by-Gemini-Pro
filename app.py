# Import necessary libraries
from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure the Google Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the prompt for Gemini model
input_prompt = """
You are an expert in understanding invoices.
We will upload an image of an invoice, and you will answer any questions based on the uploaded invoice image.
"""

# Initialize Streamlit app with custom page configuration
st.set_page_config(page_title="GeminiDecode: Multilanguage Document Extraction by Gemini Pro")

# Display header
st.header("GeminiDecode: Multilanguage Document Extraction by Gemini Pro")

# Display description
text = (
    "Utilizing Gemini Pro AI, this project effortlessly extracts vital information "
    "from diverse multilingual documents, transcending language barriers with precision "
    "and efficiency for enhanced productivity and decision-making."
)
styled_text = f"<span style='font-family:serif;'>{text}</span>"
st.markdown(styled_text, unsafe_allow_html=True)

# Text input for the prompt
input_text = st.text_input("Input Prompt:", key="input")

# File uploader for the document image
uploaded_file = st.file_uploader("Choose an image of the document:", type=["jpg", "jpeg", "png"])

# Initialize image variable
image = ""
if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Button to submit and process the document
submit = st.button("Tell me about the document")

# Function to process the uploaded image
def input_image_details(uploaded_file):
    # Open the uploaded file as a PIL Image
    image = Image.open(uploaded_file)
    # Convert the image to RGB if it's not
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return image

# Function to interact with Gemini model
def get_gemini_response(input_text, image_data, prompt):
    # Load the Gemini Pro Vision model
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Generate the response
    response = model.generate_content([input_text, image_data, prompt])
    
    # Return the response text
    return response.text if hasattr(response, 'text') else response

# If the submit button is clicked
if submit:
    if uploaded_file is not None:
        # Get the image data processed by input_image_details
        image_data = input_image_details(uploaded_file)
        
        # Get response from Gemini model
        response = get_gemini_response(input_prompt, image_data, input_text)
        
        # Display the response
        st.subheader("The response is")
        st.write(response)
    else:
        st.write("Please upload an image to proceed.")

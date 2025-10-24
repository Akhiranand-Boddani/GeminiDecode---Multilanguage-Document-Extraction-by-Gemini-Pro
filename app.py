# Import necessary libraries
import os
import streamlit as st
from PIL import Image

# Try to import Google Generative AI
GOOGLE_API_AVAILABLE = False
genai = None
try:
    import google.generativeai as genai
    GOOGLE_API_AVAILABLE = True
except ImportError as e:
    st.warning(f"Google Generative AI library not found: {e}")

# Load environment variables
# Try to get API key from Streamlit secrets first, then from environment variables
GOOGLE_API_KEY = None
if GOOGLE_API_AVAILABLE:
    try:
        GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    except:
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the Google Generative AI API only if key is available
if GOOGLE_API_KEY and GOOGLE_API_AVAILABLE:
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        API_CONFIGURED = True
    except Exception as e:
        st.error(f"Failed to configure Google Generative AI: {e}")
        API_CONFIGURED = False
else:
    API_CONFIGURED = False

# Define the prompt for Gemini model
input_prompt = """
You are an expert in understanding invoices.
We will upload an image of an invoice, and you will answer any questions based on the uploaded invoice image.
"""

def initialize_app():
    """Initialize the Streamlit app with custom page configuration."""
    st.set_page_config(
        page_title="GeminiDecode: Multilanguage Document Extraction by Gemini Pro",
        page_icon="📄",
        layout="wide"
    )

def display_header():
    """Display the app header and description."""
    st.header("GeminiDecode: Multilanguage Document Extraction by Gemini Pro")
    
    text = (
        "Utilizing Gemini Pro AI, this project effortlessly extracts vital information "
        "from diverse multilingual documents, transcending language barriers with precision "
        "and efficiency for enhanced productivity and decision-making."
    )
    styled_text = f"<span style='font-family:serif;'>{text}</span>"
    st.markdown(styled_text, unsafe_allow_html=True)

def get_user_input():
    """Get user input for the prompt and document image."""
    input_text = st.text_input("Input Prompt:", key="input")
    uploaded_file = st.file_uploader("Choose an image of the document:", type=["jpg", "jpeg", "png"])
    return input_text, uploaded_file

def display_image(image):
    """Display the uploaded image."""
    st.image(image, caption="Uploaded Image", use_column_width=True)

def process_image(uploaded_file):
    """Process the uploaded image."""
    # Open the uploaded file as a PIL Image
    image = Image.open(uploaded_file)
    # Convert the image to RGB if it's not
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return image

def get_gemini_response(input_text, image_data, prompt):
    """Interact with the Gemini model to get a response."""
    if genai is not None:
        try:
            # Load the Gemini Pro Vision model
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # Generate the response
            response = model.generate_content([input_text, image_data, prompt])
            
            # Return the response text
            return response.text if hasattr(response, 'text') else str(response)
        except Exception as e:
            return f"Error generating response: {e}"
    else:
        return "Google Generative AI is not available."

def main():
    """Main function to run the Streamlit app."""
    # Initialize the app
    initialize_app()
    
    # Display header
    display_header()
    
    # Check if Google API is available and API key is set
    if not GOOGLE_API_AVAILABLE:
        st.error("Google Generative AI library is not installed. Please install it with: pip install google-generativeai")
        st.stop()
    elif not API_CONFIGURED:
        st.warning("API key not found or configuration failed. Please set your GOOGLE_API_KEY in Streamlit secrets or environment variables.")
        st.stop()
    
    # Get user input
    input_text, uploaded_file = get_user_input()
    
    # Initialize image variable
    image = ""
    if uploaded_file is not None:
        # Process and display the uploaded image
        image = process_image(uploaded_file)
        display_image(image)
    
    # Button to submit and process the document
    submit = st.button("Tell me about the document")
    
    # If the submit button is clicked
    if submit:
        if uploaded_file is not None:
            # Get the image data processed by input_image_details
            image_data = process_image(uploaded_file)
            
            # Get response from Gemini model
            response = get_gemini_response(input_prompt, image_data, input_text)
            
            # Display the response
            st.subheader("The response is")
            st.write(response)
        else:
            st.write("Please upload an image to proceed.")

if __name__ == "__main__":
    main()
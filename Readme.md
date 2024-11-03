 GeminiDecode: Multilanguage Document Extraction by Gemini Pro

GeminiDecode is a powerful tool designed to streamline information extraction from multilingual documents, including invoices and other complex formats. It leverages Google's Gemini Pro Vision API for advanced document analysis and understanding. Users can query and retrieve structured information across languages, making it ideal for overcoming language barriers and processing large document volumes.

Features:

 Multilingual Support: Extracts content from documents in various languages using Google's Gemini AI.
 ImageBased Document Analysis: Analyze uploaded document images (JPEG, JPG, PNG) to extract details.
 RealTime Queries: Formulate custom queries to extract specific information from uploaded documents.
 UserFriendly Interface: Streamlit provides a web interface for document upload, result viewing, and model interaction.
 Prompt Design: Utilize prompts to guide Gemini AI for focused information extraction from complex documents like invoices.

Technology Stack:

 Python: Core programming language for backend logic.
 Streamlit: Framework for creating the interactive web interface.
 Google Generative AI (Gemini Pro Vision): API for imagebased generative content, specifically document processing and language support.
 Pillow (PIL): Used for image processing and handling.

Getting Started:

Before using GeminiDecode, you'll need a Google API key for Gemini Pro Vision and a Python environment.

Prerequisites:

 Google API Key: Obtain a key with access to Gemini Pro Vision and set it as an environment variable.
 Python: Ensure you have Python 3.8 or above installed.

Installation:

1. Clone the Repository:

bash
git clone https://yourusername/geminidecode.git
cd geminidecode


2. Set Up Environment Variables:

 Create a `.env` file in the project directory.
 Add your Google API key to the `.env` file:

plaintext
GOOGLE_API_KEY=your_google_api_key


3. Install Dependencies:

Install required Python packages using `pip`:

bash
pip install r requirements.txt


4. Run the Streamlit App:

bash
streamlit run app.py


Usage:

1. Launch the Application: After running the app, it will open in your web browser.
2. Upload a Document: Use the file uploader to select a document image (JPEG, JPG, or PNG).
3. Enter a Query Prompt: Specify the information you want to extract from the document.
4. Submit and View Results: Click "Tell me about the document" to get a response based on your input.

Example Scenarios:

 Invoice Processing: Upload an invoice image and query for specific fields like "total amount," "invoice date," or "billing address."
 Multilingual Document Handling: Extract and translate information from documents written in other languages, like invoices from international suppliers.
 Automated Data Extraction: Query tables, item lists, or specific details from documents for integration into other systems or reports.

Future Enhancements:

 Enhanced Language Support: Expand support for additional languages and dialects.
 Data Export Options: Allow users to export extracted information in CSV, PDF, or JSON formats.
 User Authentication: Add user roles and permissions for secure access in multiuser environments.
 Cloud Storage Integration: Store documents in Google Drive or AWS S3 for streamlined access and document management.

Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of your changes.

License

This project is licensed under the MIT License. See the [LICENSE] file for more details.

This revised version removes unnecessary markups and focuses on clear, concise text for improved readability. 
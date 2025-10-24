# GeminiDecode: Multilanguage Document Extraction by Gemini Pro

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Streamlit](https://img.shields.io/badge/streamlit-1.31%2B-red)

GeminiDecode is a powerful tool designed to streamline information extraction from multilingual documents, including invoices and other complex formats. It leverages Google's Gemini Pro Vision API for advanced document analysis and understanding. Users can query and retrieve structured information across languages, making it ideal for overcoming language barriers and processing large document volumes.

<p align="center">
  <img src="Images/GeminiDecode_Demo.png" alt="GeminiDecode Demo" width="600"/>
</p>

## 🌟 Features

- **Multilingual Support**: Extracts content from documents in various languages using Google's Gemini AI.
- **Image-Based Document Analysis**: Analyze uploaded document images (JPEG, JPG, PNG) to extract details.
- **Real-Time Queries**: Formulate custom queries to extract specific information from uploaded documents.
- **User-Friendly Interface**: Streamlit provides a web interface for document upload, result viewing, and model interaction.
- **Prompt Design**: Utilize prompts to guide Gemini AI for focused information extraction from complex documents like invoices.
- **Secure API Management**: Safely handle API keys through environment variables or Streamlit secrets.

## 🛠️ Technology Stack

- **Python**: Core programming language (3.8+)
- **Streamlit**: Framework for creating the interactive web interface (1.31+)
- **Google Generative AI (Gemini Pro Vision)**: API for image-based generative content (0.7.0+)
- **Pillow (PIL)**: Image processing and handling (10.0.0+)
- **LangChain**: Prompt handling and LLM integration (0.2.0+)
- **PyPDF2**: PDF file processing capabilities (3.0.1+)
- **ChromaDB**: Vector databases for embedding storage (0.5.0+)
- **FAISS-CPU**: Vector databases for embedding storage (1.8.0+)

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or above
- Google API Key with access to Gemini Pro Vision
- pip package manager

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/geminidecode.git
   cd geminidecode
   ```

2. **Set Up Environment Variables**:
   
   Create a `.env` file in the project directory:
   ```bash
   touch .env
   ```
   
   Add your Google API key to the `.env` file:
   ```
   GOOGLE_API_KEY=your_actual_google_api_key_here
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## ☁️ Deployment

### Streamlit Cloud Deployment

1. Push your code to a GitHub repository
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and create a new app
3. Connect your GitHub repository
4. Set your `GOOGLE_API_KEY` in the Secrets section:
   - Go to your app settings
   - In the "Secrets" section, add: `GOOGLE_API_KEY = "your_actual_key_here"`
5. Deploy the app

### Required Files for Deployment

- `requirements.txt` - Python dependencies
- `.streamlit/config.toml` - Streamlit configuration
- `.streamlit/secrets.toml` - Template for API keys (do not commit actual keys)

## 📖 Usage

1. **Launch the Application**: After running the app, it will open in your web browser.
2. **Upload a Document**: Use the file uploader to select a document image (JPEG, JPG, or PNG).
3. **Enter a Query Prompt**: Specify the information you want to extract from the document.
4. **Submit and View Results**: Click "Tell me about the document" to get a response based on your input.

### Example Queries

- "What is the total amount on this invoice?"
- "Extract the billing address from this document"
- "List all items and their prices"
- "What is the invoice date?"
- "Translate the vendor name to English"

## 📋 Example Scenarios

### Invoice Processing
Upload an invoice image and query for specific fields like "total amount," "invoice date," or "billing address."

### Multilingual Document Handling
Extract and translate information from documents written in other languages, like invoices from international suppliers.

### Automated Data Extraction
Query tables, item lists, or specific details from documents for integration into other systems or reports.

## 📁 Project Structure

```
geminidecode/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
├── Images/
│   └── GeminiDecode_Demo.png
├── .env
├── .gitignore
├── LICENSE
├── Readme.md
├── requirements.txt
├── app.py
└── packages.txt
```

## 🧪 Testing

To test the application locally:

1. Ensure all dependencies are installed
2. Set up your API key in the `.env` file
3. Run the application with `streamlit run app.py`
4. Upload a sample document and test various queries

## 🤝 Contributing

We welcome contributions from the community! Here's how you can contribute:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them with clear, descriptive messages
4. Push your changes to your fork
5. Submit a pull request with a clear description of your changes

### Development Guidelines

- Follow PEP 8 style guidelines for Python code
- Write clear, descriptive commit messages
- Test your changes thoroughly before submitting a pull request
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/geminidecode/issues) section
2. Create a new issue if your problem hasn't been reported
3. Provide detailed information about the problem, including:
   - Error messages
   - Steps to reproduce
   - Environment details (OS, Python version, etc.)

## 🙏 Acknowledgments

- Google Generative AI team for the Gemini Pro Vision API
- Streamlit team for the excellent web framework
- All contributors who have helped improve this project

---

<p align="center">
  Made with ❤️ using Python, Streamlit, and Google Gemini Pro Vision
</p>
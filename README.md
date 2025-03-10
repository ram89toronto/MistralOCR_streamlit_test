# OCR Mistral

## Project Overview

OCR Mistral is a Streamlit application that allows users to upload PDF documents and extract text in Markdown format using the Mistral OCR API. This project leverages the capabilities of the Mistral API to provide accurate text extraction from PDF files.

## Features
- Upload PDF files for OCR processing.
- Extracted text is displayed in Markdown format.
- Option to download the extracted Markdown text.
- User-friendly interface with API key input in the sidebar.

## Installation Instructions
To run this application, you need to install the required packages. Use the following command:
```bash
pip install streamlit mistralai PyPDF2
```

## Usage Instructions
1. **Run the Application**: Start the Streamlit application using the following command:
   ```bash
   streamlit run app.py
   ```
2. **Enter API Key**: In the sidebar, enter your Mistral API key to authenticate.
3. **Upload PDF**: Use the file uploader to select a PDF document.
4. **Submit for Processing**: Click the "Submit" button to process the document.
5. **View Extracted Text**: The extracted text will be displayed in Markdown format.
6. **Download Markdown**: Optionally, download the extracted text as a Markdown file.

## API Key
To use the Mistral API, you need to obtain an API key. Replace the placeholder in the code with your actual API key.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request.

## License
This project is licensed under the MIT License.
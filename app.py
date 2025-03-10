import streamlit as st
from mistralai import Mistral
from pathlib import Path
import json

# Streamlit app title
st.title('PDF to Markdown with Mistral OCR')

# Sidebar for API key input
api_key = st.sidebar.text_input('Enter Mistral API Key', type='password')

# Set up the Mistral client
if api_key:
    client = Mistral(api_key=api_key)
else:
    st.warning('Please enter your Mistral API key to proceed.')

# Input for PDF upload
uploaded_file = st.file_uploader('Choose a PDF file', type='pdf')

# Button to submit the document for processing
if st.button('Submit') and uploaded_file is not None and api_key:
    # Upload the document for OCR processing
    uploaded_file_response = client.files.upload(
        file={
            'file_name': uploaded_file.name,
            'content': uploaded_file.read(),
        },
        purpose='ocr',
    )
    signed_url = client.files.get_signed_url(file_id=uploaded_file_response.id, expiry=1)

    # Specify model
    model = 'mistral-small-latest'  # Dedicated OCR capabilities

    # Define query with the uploaded document
    messages = [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': 'Extract specific information from this document.'  # Customize your query
                },
                {
                    'type': 'document_url',
                    'document_url': signed_url.url
                }
            ]
        }
    ]

    # Get the response
    chat_response = client.chat.complete(
        model=model,
        messages=messages
    )

    # Extract markdown from the response
    all_markdown = chat_response.choices[0].message.content

    # Display the extracted markdown
    st.markdown(all_markdown)

    # Optionally, allow users to download the markdown
    st.download_button(
        label='Download Markdown',
        data=all_markdown,
        file_name='extracted_markdown.md',
    )
else:
    if uploaded_file is not None:
        st.warning('Please enter your Mistral API key to proceed.')

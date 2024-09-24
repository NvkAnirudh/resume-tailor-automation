import streamlit as st
import sys
import os
import tempfile
import uuid
import webbrowser
from urllib.parse import urlencode
# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from src.resume_analyzer import optimize_resume
from src.pdf_handler import read_pdf
from src.google_docs_api_processing import google_docs_auth, create_google_doc
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

st.set_page_config(page_title="Resume Optimizer", layout="wide")

# Create a directory to store uploaded files
UPLOAD_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_resumes')
os.makedirs(UPLOAD_DIR, exist_ok=True)

def create_pdf(text):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    y = height - 50  # Start near the top of the page
    for line in text.split('\n'):
        if y < 50:  # If we're near the bottom of the page
            c.showPage()  # Start a new page
            y = height - 50  # Reset y to the top of the new page
        c.drawString(50, y, line)
        y -= 15  # Move down for the next line
    c.save()
    buffer.seek(0)
    return buffer

def save_uploaded_file(uploaded_file):
    """Save the uploaded file and return the file path."""
    try:
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.getvalue())
        return file_path
    except Exception as e:
        st.error(f"An error occurred while saving the file: {str(e)}")
        return None

def main():
    st.title("Resume Optimizer")

    # File upload and manual entry option
    upload_option = st.radio("Choose how to input your resume:", ("Upload PDF", "Enter manually"))

    resume_content = None
    if upload_option == "Upload PDF":
        resume_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
        if resume_file is not None:
            file_path = save_uploaded_file(resume_file)
            if file_path:
                resume_content = read_pdf(file_path)
                if resume_content.startswith("An error occurred"):
                    st.error(resume_content)
                    resume_content = None
                else:
                    st.success("PDF successfully read!")
                    st.text_area("Extracted Content", resume_content, height=200, placeholder="Your resume content will appear here...")
                # Clean up: remove the file after reading
                os.remove(file_path)
    else:
        resume_content = st.text_area("Enter your resume text", height=300, placeholder="Paste or type your resume here...")

    job_description = st.text_area("Enter the job description", placeholder="Paste the job description here...")

    # Create a container for buttons with custom CSS
    button_container = st.container()
    with button_container:
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            optimize_button = st.button("Optimize Resume")
        
        with col2:
            open_in_google_docs_button = st.button("Open in Google Docs")

    # Add custom CSS to style the buttons
    st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        margin-right: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Initialize session state for storing results
    if 'analysis_dict' not in st.session_state:
        st.session_state.analysis_dict = None
    if 'updated_resume' not in st.session_state:
        st.session_state.updated_resume = None

    if optimize_button and resume_content and job_description:
        with st.spinner("Analyzing and optimizing your resume..."):
            st.session_state.analysis_dict, st.session_state.updated_resume = optimize_resume(resume_content, job_description)
        
        if st.session_state.analysis_dict and st.session_state.updated_resume:
            st.success("Analysis complete!")
            display_results()
        else:
            st.error("An error occurred during analysis. Please try again.")

    if open_in_google_docs_button and st.session_state.updated_resume:
        # Authenticate and create Google Docs API service
        service = google_docs_auth()

        # Create a Google Doc and get its URL
        doc_url = create_google_doc(service, st.session_state.updated_resume)

        st.success('Google Doc created successfully')
        st.write(f'[Open the Google Doc]({doc_url})')

        # Open the document in the browser
        webbrowser.open(doc_url)

        # Display results again to keep them visible
        display_results()

def display_results():
    if st.session_state.analysis_dict and st.session_state.updated_resume:
        # Display analysis results
        for key, value in st.session_state.analysis_dict.items():
            st.subheader(key.replace('_', ' ').title())
            if isinstance(value, list):
                for item in value:
                    st.write(f"- {item}")
            else:
                st.write(value)
        
        # Display updated resume
        st.subheader("Updated Resume")
        st.text_area("", value=st.session_state.updated_resume, height=300, placeholder="Your optimized resume will appear here...")

if __name__ == "__main__":
    main()
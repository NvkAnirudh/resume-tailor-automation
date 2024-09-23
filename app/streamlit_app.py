import streamlit as st
import sys
import os
import tempfile
import uuid
# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from src.resume_analyzer import optimize_resume
from src.pdf_handler import read_pdf
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
        # file_extension = os.path.splitext(uploaded_file.name)[1]
        # file_name = f"{uuid.uuid4()}{file_extension}"
        # file_path = os.path.join(UPLOAD_DIR, file_name)
        # with open(file_path, "wb") as f:
        #     f.write(uploaded_file.getvalue())
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
                    st.text_area("Extracted Content", resume_content, height=200)
                # Clean up: remove the file after reading
                os.remove(file_path)
    else:
        resume_content = st.text_area("Enter your resume text", height=300)

    job_description = st.text_area("Enter the job description")

    # Always display buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        optimize_button = st.button("Optimize Resume")
    
    with col2:
        download_pdf_button = st.button("Download Optimized Resume (PDF)")
    
    with col3:
        download_txt_button = st.button("Download Optimized Resume (TXT)")

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
            st.text_area("", value=st.session_state.updated_resume, height=300)
        else:
            st.error("An error occurred during analysis. Please try again.")

    if download_pdf_button and st.session_state.updated_resume:
        pdf_buffer = create_pdf(st.session_state.updated_resume)
        st.download_button(
            label="Download Optimized Resume (PDF)",
            data=pdf_buffer,
            file_name="optimized_resume.pdf",
            mime="application/pdf"
        )

    if download_txt_button and st.session_state.updated_resume:
        st.download_button(
            label="Download Optimized Resume (TXT)",
            data=st.session_state.updated_resume,
            file_name="optimized_resume.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()
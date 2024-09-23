import streamlit as st
import pdfplumber
import os

# Define the folder path to save uploaded files
UPLOAD_FOLDER = 'uploads'

def read_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

def main():
    st.title("PDF Text Extractor")
    st.markdown("Upload a PDF file to extract its text.")

    # Create upload folder if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # Create file uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file:
        # Save uploaded file to the upload folder
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.getvalue())

        # Read PDF text
        text = read_pdf(file_path)

        # Display PDF text
        st.write("Extracted Text:")
        st.markdown(text)

        # Optional: Delete the uploaded file after processing
        # os.remove(file_path)

if __name__ == "__main__":
    main()


# import streamlit as st
# import pdfplumber
# import io

# def read_pdf(file_buffer):
#     with pdfplumber.open(io.BytesIO(file_buffer)) as pdf:
#         text = ''
#         for page in pdf.pages:
#             text += page.extract_text()
#     return text

# def main():
#     st.title("PDF Text Extractor")
#     st.markdown("Upload a PDF file to extract its text.")

#     # Create file uploader
#     uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

#     if uploaded_file:
#         # Read PDF text
#         text = read_pdf(uploaded_file.getvalue())

#         # Display PDF text
#         st.write("Extracted Text:")
#         st.markdown(text)

# if __name__ == "__main__":
#     main()
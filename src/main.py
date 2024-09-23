from resume_analyzer import optimize_resume
from pdf_handler import read_pdf
from config import ANTHROPIC_API_KEY
import pathlib
from pathlib import Path

# Read resume
resume_file_path = pathlib.Path(__file__).parent.parent / 'data' / 'sample_resumes' / 'Anirudh_Nuti_DA.pdf'

print(pathlib.Path(__file__).parent.parent / 'data' / 'sample_resumes')
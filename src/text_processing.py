import re
import ast

def text_processing(text):
    # Regular expressions to extract resume_analysis and the updated resume
    resume_analysis_pattern = re.compile(r'resume_analysis\s*=\s*({.*?})', re.DOTALL)
    updated_resume_pattern = re.compile(r"Here's an updated version of your resume, optimized for the given job description:\n\n(.*)", re.DOTALL)

    # print(resume_analysis_pattern)

    # Extract resume_analysis
    resume_analysis_match = resume_analysis_pattern.search(text)
    resume_analysis = resume_analysis_match.group(1) if resume_analysis_match else None

    # Extract updated resume
    updated_resume_match = updated_resume_pattern.search(text)
    updated_resume = updated_resume_match.group(1) if updated_resume_match else None

    # Convert the resume_analysis string to a Python dictionary
    resume_analysis = ast.literal_eval(resume_analysis) if resume_analysis else None

    return resume_analysis, updated_resume
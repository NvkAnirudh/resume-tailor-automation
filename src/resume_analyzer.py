from api_client import call_claude_api
from text_processing import text_processing
import json

def optimize_resume(resume_content, job_description):
    prompt = f"""
    I'm actively applying for jobs and want to optimize my resume for Applicant Tracking Systems (ATS) to increase my chances of getting interviews. 
    My goal is to achieve an ATS score of 85% or higher. Please help me with the following: Analyze my current resume (attached) and the target job 
    description (also provided below). Identify any areas where keywords, skills, or formatting could be improved to better align with the job requirements
    and ATS algorithms. Revise my resume based on your analysis. Incorporate relevant keywords, highlight key accomplishments with strong action verbs, 
    and ensure the formatting is ATS-friendly. Offer additional suggestions for optimizing my resume content or layout, if applicable. At the end, give me 
    the predicted ATS score for the job description and the updated resume. Also keep the projects that are relevant and remove the rest and tell me which 
    ones are not relevant so that I can remove them. And, if possible add additional projects or skills that you think are relevant and may add more weight 
    to the resume and tell me what resumes you have added. Please provide an updated resume. Start the updated resume section with this heading 'Here's an updated version of your resume, 
    optimized for the given job description:'

    # I'm actively applying for jobs and want to optimize my resume for Applicant Tracking Systems (ATS) to increase my chances of getting interviews. My goal is to achieve an ATS score of 85% or higher. Please help me with the following:

    # 1. Analyze my current resume and the target job description provided below.
    # 2. Identify any areas where keywords, skills, or formatting could be improved to better align with the job requirements and ATS algorithms.
    # 3. Revise my resume based on your analysis. Incorporate relevant keywords, highlight key accomplishments with strong action verbs, and ensure the formatting is ATS-friendly.
    # 4. Offer additional suggestions for optimizing my resume content or layout, if applicable.
    # 5. Provide a predicted ATS score for the job description and the updated resume.
    # 6. Identify any projects in the resume that may not be relevant to this specific job application and only keep 3-4 project (max) in the updated resume.
    # 7. Provide an updated version of the resume. Start the updated resume section with this heading 'Here's an updated version of your resume, optimized for the given job description:'

    Please present your analysis and suggestions in a structured Python dictionary format, similar to the following:

    # resume_analysis = {{
    #     "ats_score": 0,
    #     "keyword_suggestions": [],
    #     "formatting_suggestions": [],
    #     "content_improvements": [],
    #     "irrelevant_projects": []
    # }}

    resume_analysis = {{
        "ats_score": 0,
        "keyword_and_skills_alignment": [],
        "relevant_projects_and_experience": [],
        "additional_suggestions": [],
        "changes_and_optimizations": [],
        "updated_ats_score": 0
    }}

    Current Resume: {resume_content}
    Job Description: {job_description}
    """

    response = call_claude_api(prompt)
    response = response[0].text
    # print(response)

    # Extract the dictionary and updated resume
    try:
        return text_processing(response)
    except:
        return None, None
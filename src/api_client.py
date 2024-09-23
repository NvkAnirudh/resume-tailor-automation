import anthropic
from config import ANTHROPIC_API_KEY

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def call_claude_api(prompt):
    response = client.messages.create(
        model='claude-3-5-sonnet-20240620',
        max_tokens=3000,
        temperature=0,
        system="You are a resume optimization expert. Optimize the attached resume to achieve an ATS score of 85% or higher for the target job description. Provide a revised resume, predicted ATS score, and suggestions for improvement.",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content
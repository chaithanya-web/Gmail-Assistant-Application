import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def summarize_email(email_content):
    prompt = f"Summarize this email:\n\n{email_content}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7  # Adjust for creativity level
    )

    return response.choices[0].message["content"]  # Updated response handling

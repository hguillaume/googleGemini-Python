# pip install google-genai

# Create API Key Here: https://aistudio.google.com/app/api-keys

from google import genai
from google.genai import types
import googleGeminiAPIKey

client = genai.Client(api_key=googleGeminiAPIKey.api_key)

# List of Google Gemini models:  https://ai.google.dev/gemini-api/docs/models#gemini-2.0-flash
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents='Why is the sky blue?'
    # model='gemini-2.5-flash', contents='Why is the sky blue?'
    # model='gemini-2.5-flash-lite', contents='Why is the sky blue?
    # model='gemini-2.5-pro', contents='Why is the sky blue?'
)
print(response.text)
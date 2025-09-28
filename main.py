# pip install google-genai

# Create API Key Here: https://aistudio.google.com/app/api-keys

from google import genai
from google.genai import types
import googleGeminiAPIKey

client = genai.Client(api_key=googleGeminiAPIKey.api_key)

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents='Why is the sky blue?'
)
print(response.text)
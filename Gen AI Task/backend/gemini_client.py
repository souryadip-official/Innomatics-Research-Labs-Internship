import google.generativeai as genai
from config import Config

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=Config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(Config.MODEL_NAME)

    def generate_response(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text
from backend.gemini_client import GeminiClient
from prompts.system_prompt import PromptBuilder

class ChatService:
    def __init__(self):
        self.client = GeminiClient()

    def get_response(self, chat_history):
        prompt = PromptBuilder.build_prompt(chat_history)
        response = self.client.generate_response(prompt)
        return response
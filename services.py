from google import genai

class AIService:
    def __init__(self):
        self.Client = genai.Client()

    def generate_reply(self,prompt):
        response = self.Client.models.generate_content(
            model = "gemini-2.5-flash", contents=prompt
        )
        return response.text 


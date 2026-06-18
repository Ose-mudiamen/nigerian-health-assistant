import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class HealthChatbot:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.conversation_history = []
        self.system_prompt = """ You are a helpful Nigerian healthcare assistant.
        You help everyday Nigerians understand their symptoms and decide whether
        to rest at home, visit a pharmacy, or go to the hosiptal.
        Always ask clarifying questions about symptoms.
        Be warm, clear, and speak in simple English. """
    
    def chat(self, user_message):
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": self.system_prompt},
                *self.conversation_history
            ]
        )
        assistant_message = response.choices[0].message.content

        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        return assistant_message
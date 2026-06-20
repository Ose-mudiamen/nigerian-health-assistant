import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class HealthChatbot:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.conversation_history = []
        self.system_prompt = """You are a Nigerian Healthcare AI Assistant specialized in helping everyday Nigerians understand their health systoms.
        After gathering enough information, always respond with a structured assessment in this exact format:
        
        **ASSESSMENT**
        - Possible Conditions: [condition name]
        - Severity: [Mild/ Moderate/ Serious]
        - Recommended Action: [Rest at home/ Visit a Pharmacy/ Go to a hosiptal immediately]
        - Warning Signs: [signs that mean they need urgent care]
        
        **EXPLANATION**
        [Brief plain English explanation of what might be going on]
        
        Key Nigerian diseases consider: malaria, cholera, typhoid, hypertension, sickle cell crisis, peptic ulcer, meningitis.
        
        Always ask at least one clarifying question before giving an assessment. Be warm, clear and speak in simple English."""
        
    
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
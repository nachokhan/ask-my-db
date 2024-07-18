import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file located in ./conf/
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.conf/.env'))


class GPTConnector:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self._client = OpenAI()

    def send_prompt(self, user_prompt):
        try:
            prompt = f'Respond without introductions or conclusions. Only provide the precise information I request without any kind of formatting, just raw text: {user_prompt}'
            messages = [
                {"role": "user", "content": prompt}
            ]
            response = self._client.chat.completions.create(
                model="gpt-4o",
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

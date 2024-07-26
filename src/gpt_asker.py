import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file located in ./conf/
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.conf/.env'))


class GPTAsker:
    def __init__(self):
        """
        Initializes the GPTAsker with the OpenAI API key.
        """
        self.api_key = os.getenv('OPENAI_API_KEY')
        self._client = OpenAI()

    def send_prompt(self, user_prompt):
        """
        Sends a prompt to the GPT model and returns the response.

        Args:
            user_prompt (str): The user's prompt to send to GPT.

        Returns:
            str: The response from GPT.
        """
        try:
            prompt = f'Respond without introductions or conclusions. Only provide the precise information I request without any kind of formatting, just raw text: {user_prompt}'
            messages = [
                {"role": "user", "content": prompt}
            ]
            response = self._client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=0.1,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

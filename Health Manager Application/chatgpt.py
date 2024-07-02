import openai

class OpenAIChatbot:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.input_prompt = None
        self.chat_response = None

    def get_response(self, input_prompt):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=input_prompt,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        self.input_prompt = input_prompt
        self.chat_response = response.choices[0].text.strip()
        return self.chat_response
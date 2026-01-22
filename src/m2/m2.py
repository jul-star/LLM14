from openai import Client, OpenAI
from openai import OpenAIError, AuthenticationError
import os

_api_key = os.environ.get('OPENAI_API_KEY')

# https://platform.openai.com/docs/overview


from openai import OpenAI

client = OpenAI(
  api_key=_api_key
)

response = client.responses.create(
  model="gpt-5-nano",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);

import os
from ollama import Client
from src.utils.logging_config import setup_logging
import logging  
setup_logging("m1_cloud.log")
logger = logging.getLogger(__name__)

_api_key    = os.environ.get('OLLAMA_API_KEY')
print(f"API Key: {_api_key}")

client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + _api_key}
)

messages = [
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
]

# for part in client.chat('gpt-oss:120b', messages=messages, stream=True):
#   print(part['message']['content'], end='', flush=True)
  
  
for part in client.chat('deepseek-v3.1:671b-cloud', messages=messages, stream=True):
  print(part['message']['content'], end='', flush=True) 
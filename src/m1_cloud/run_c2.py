from ollama import Client

#FIXME: No luck!

client = Client()

messages = [
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
]

# for part in client.chat('gpt-oss:120b-cloud', messages=messages, stream=True):
#   print(part['message']['content'], end='', flush=True)
  
  
  
for part in client.chat('deepseek-v3.1:671b-cloud', messages=messages, stream=True):
  print(part['message']['content'], end='', flush=True) 
  
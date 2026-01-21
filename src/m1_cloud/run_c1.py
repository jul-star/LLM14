import requests
import os
import logging
from src.utils.logging_config import setup_logging
setup_logging("m1_cloud.log")
logger = logging.getLogger(__name__)

def main_cloud():
    api_key = os.getenv("OLLAMA_API_KEY")
    if not api_key:
        print("Ошибка: OLLAMA_API_KEY не установлен")
        return
    
    # Правильный endpoint Ollama Cloud
    url = "https://ollama.com/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "deepseek-v3.1:671b",
        "messages": [
            {
                "role": "user",
                "content": "Привет DeepSeek! Скажи пару слов о себе."
            }
        ],
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Проверка на ошибки HTTP
        
        result = response.json()
        print(result["choices"][0]["message"]["content"])
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            print("Ошибка аутентификации: проверьте API ключ")
        else:
            print(f"HTTP ошибка: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == '__main__':
    main_cloud()
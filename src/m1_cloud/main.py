from ollama import Client
import os
from src.utils.logging_config import setup_logging
import logging
import time

setup_logging("m1_cloud.log")
logger = logging.getLogger(__name__)

def main():
    # Установка API ключа
    # os.environ['OLLAMA_API_KEY'] = 'ваш_api_ключ'
    _api_key = os.getenv("OLLAMA_API_KEY")
    logger.info(f"key: {_api_key}")
    if not _api_key:
        print("Api key not set!")
        return
    # Создание клиента Ollama Cloud
    client = Client(
        host='https://ollama.com',
        headers={
            'Authorization': f'Bearer {_api_key}'
        }
    )
    time.sleep(5)
    
    if not client:
        print("Can't create client!")
        logger.error(f"Can't create client!")
        return 
    
    # Отправка запроса
    response = client.chat(
        model='deepseek-v3.1:671b-cloud',  # указываем облачную модель
        messages=[
            {
                "role": "user",
                "content": "Привет DeepSeek! Скажи пару слов о себе."
            }
        ]
    )
    
    # Вывод результата
    print(response.message.content)

if __name__ == '__main__':
    main()

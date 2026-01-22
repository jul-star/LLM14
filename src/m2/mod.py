from openai import OpenAI
import time
from typing import Optional

client = OpenAI()

def moderate(text: str, max_retries: int = 3) -> bool:
    """Return True if content is safe (not flagged)."""
    for attempt in range(max_retries):
        try:
            result = client.moderations.create(input=text, model="omni-moderation-latest")
            return not result.results[0].flagged
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Ошибка модерации: {e}. Попытка {attempt + 1} из {max_retries}")
                time.sleep(2 ** attempt)  # экспоненциальная задержка
            else:
                raise

def get_response(message: str, max_retries: int = 3) -> Optional[str]:
    """Получить ответ от модели с обработкой ошибок."""
    for attempt in range(max_retries):
        try:
            reply = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": message}]
            )
            return reply.choices[0].message.content
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Ошибка при получении ответа: {e}. Попытка {attempt + 1} из {max_retries}")
                time.sleep(2 ** attempt)  # экспоненциальная задержка
            else:
                raise

user_msg = "write a haiku about ai"  # input(">>> ")

try:
    if not moderate(user_msg):
        print("❗ Message blocked by policy.")
    else:
        reply = get_response(user_msg)
        if reply:
            print(reply)
except Exception as e:
    print(f"Критическая ошибка: {e}")

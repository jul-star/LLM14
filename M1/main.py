from openai import OpenAI

def main():
    # Инициализация клиента (указываем URL LocalAI)
    client = OpenAI(
        base_url="http://localhost:8080/v1",
        api_key="not-required"  # LocalAI не требует ключа
    )

    # Отправка запроса
    chat_completion = client.chat.completions.create(
        model="qwen3-vl-4b-instruct",  # имя из models.yaml
        messages=[
            {"role": "user", "content": "Напиши краткий гайд по работе с LocalAI"}
        ],
        temperature=0.7,
        max_tokens=300
    )
    print(chat_completion.choices[0].message.content)

if __name__ == '__main__':
    main()
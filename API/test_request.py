import requests

# URL вашего API
api_url = "http://127.0.0.1:5000/search_relatives"

# Параметры запроса (фамилия и город)
params = {"last_name": "Штейнер", "city": "Воронеж"}
params = {"last_name": "Федотов", "city": "Екатеринбург"}

# Отправляем GET-запрос к API
response = requests.post(api_url, json=params)

# Проверяем статус ответа
if response.status_code == 200:
    # Распечатываем результат
    data = response.json()
    print("Результат поиска родственников:")
    for relative in data["results"]:
        print(f"ФИО: {relative['full_name']}, Ник в Telegram: {relative['telegram_username']}")
else:
    print(f"Ошибка: {response.status_code} - {response.text}")
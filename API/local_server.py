from flask import Flask, request, jsonify

app = Flask(__name__)

# Пример базы данных родственников (замените на свою реальную базу данных)
relatives_db = [
    {"last_name": "Федотов", "city": "Екатеринбург", "full_name": "Фёдор Федотов", "telegram_username": "@john"},
    {"last_name": "Штейнер", "city": "Воронеж", "full_name": "Мария Штейнер", "telegram_username": "@alice"},
]

@app.route('/search_relatives', methods=['POST'])
def search_relatives():
    data = request.get_json()

    if "last_name" not in data or "city" not in data:
        return jsonify({"error": "Необходимо указать фамилию и город в запросе."}), 400

    last_name = data["last_name"]
    city = data["city"]

    results = []

    for relative in relatives_db:
        if relative["last_name"] == last_name and relative["city"] == city:
            results.append({"full_name": relative["full_name"], "telegram_username": relative["telegram_username"]})

    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)
storage = {}

@app.route('/add/<date>/<int:number>')
def add_expense(date, number):
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:8])

    storage.setdefault(year, {}).setdefault(month, {})
    storage[year][month][day] = storage[year][month].get(day, 0) + number

    return f"Добавлена трата {number} руб. за {day}.{month}.{year}"

@app.route('/calculate/<int:year>')
def calculate_year(year):
    if year not in storage:
        return f"Нет данных за {year} год"

    total = 0
    for month in storage[year]:
        for day in storage[year][month]:
            total += storage[year][month][day]

    return f"Суммарные траты за {year} год: {total} руб."

@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year, month):
    if year not in storage or month not in storage[year]:
        return f"Нет данных за {month}.{year}"

    total = sum(storage[year][month].values())
    return f"Суммарные траты за {month}.{year}: {total} руб."

if __name__ == '__main__':
    app.run(debug=True)
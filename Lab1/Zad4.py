from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def show_current_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    return f'Точное время: {current_time}'

if __name__ == '__main__':
    app.run()




# ## Задача 4. /get_time/now
# ### Что нужно сделать
# Создайте страницу с текстом `«Точное время: {current_time}»`, где `current_time` — точное текущее время.
# ### Советы и рекомендации
# Получить точное время можно с помощью функции [now()](https://docs.python.org/3/library/datetime.html#datetime.datetime.now) из модуля `datetime.datetime`.
# ### Что оценивается
# - При форматировании строк используются переменные, а не выражения.
# - При обновлении страницы время также обновляется.
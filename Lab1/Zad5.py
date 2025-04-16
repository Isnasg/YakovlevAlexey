from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def show_future_time():
    now = datetime.now()

    future_time = now + timedelta(hours=1)

    current_time_after_hour = future_time.strftime('%H:%M:%S')
    return f'Точное время через час будет {current_time_after_hour}'

if __name__ == '__main__':
    app.run()




# ## Задача 5. /get_time/future
# ### Что нужно сделать
# Создайте страницу с текстом `«Точное время через час будет {current_time_after_hour}»`, где `current_time_after_hour` — точное время через один час.
# ### Советы и рекомендации
# Получить точное время через час можно с помощью класса [timedelta](https://docs.python.org/3/library/datetime.html#timedelta-objects) из модуля `datetime`.
# ### Что оценивается
# - При форматировании строк используются переменные, а не выражения.
# - При обновлении страницы время также обновляется.
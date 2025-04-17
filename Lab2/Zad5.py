from flask import Flask, abort

app = Flask(__name__)

@app.route('/<path:numbers>')
def max_number(numbers):
    try:
        num_list = [int(num) for num in numbers.split('/')]
    except ValueError:
        abort(400, description="Переданы некорректные данные. Ожидались числа, разделенные слешем.")

    if not num_list:
        abort(400, description="Не передано ни одного числа.")

    max_num = max(num_list)
    return f"Максимальное число: <i>{max_num}</i>"

if __name__ == '__main__':
    app.run()
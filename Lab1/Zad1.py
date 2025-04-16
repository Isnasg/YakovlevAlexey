from flask import Flask
app = Flask(__name__)

@app.route('/')
def f():
    return'Привет Мир!'
app.run()

# ## Задача 1. /hello_world
# ### Что нужно сделать
# Создайте страницу с текстом «Привет, мир!».
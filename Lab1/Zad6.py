from flask import Flask
import os
import re
import random

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

words = []

def load_words():
    global words
    try:
        with open(BOOK_FILE, 'r', encoding='utf-8') as file:
            text = file.read()
            # Извлекаем только слова на кириллице без пунктуации
            words = re.findall(r'\b[а-яёА-ЯЁ]+\b', text)
    except FileNotFoundError:
        words = []  # Оставляем пустым, если файл не найден

load_words()

@app.route('/')
def get_random_word():
    if not words:
        return "Файл с книгой не найден или не содержит слов", 404
    return random.choice(words)

if __name__ == '__main__':
    app.run()



# ## Задача 6. /get_random_word
# ### Что нужно сделать
# Создайте страницу со случайным словом из книги «Война и мир» Льва Толстого. Книга лежит в одной папке с практическим
# заданием и называется `war_and_peace.txt`.
# ### Советы и рекомендации
# - Для получения случайного слова можно также воспользоваться модулем `random`.
# - Для получения списка слов из текста могут понадобиться [регулярные выражения](https://tproger.ru/translations/regular-expression-python/).
# - Если запустить программу из другой директории, то при обращении к `/get_random_word` возникнет ошибка
# `FileNotFoundError`. Это связано с тем, что заданный к файлу путь является относительным, то есть он зависит от текущей
# рабочей директории. Чтобы этого избежать, можно создать переменную `BASE_DIR`, которая содержит абсолютный путь к папке
# проекта, а затем уже от него задавать путь к файлу.
# ```python
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')
#
# with open(BOOK_FILE) as book:
# ```
# - Подумайте, нужно ли открывать файл `war_and_peace.txt` каждый раз при обращении к странице `/get_random_word`?
# ### Что оценивается
# - Слово отображается без знаков препинания.
# - При запуске программы из другой директории и наличии файла `war_and_peace.txt` не выводится ошибка.
# - Получение списка слов вынесено в отдельную функцию.
# - При обращении к странице файл не открывается заново.
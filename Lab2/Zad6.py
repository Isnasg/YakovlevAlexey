from flask import Flask, abort
import os

app = Flask(__name__)

@app.route('/<int:size>/<path:relative_path>')
def file_preview(size, relative_path):
    try:
        abs_path = os.path.abspath(relative_path)

        with open(abs_path, 'r', encoding='utf-8') as file:
            preview_text = file.read(size)
            actual_size = len(preview_text)

        return (f"<b>{abs_path}</b> {actual_size}<br>"
                f"{preview_text}")

if __name__ == '__main__':
    app.run()
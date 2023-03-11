import os
from flask import Flask

app = Flask(__name__)


@app.route('/preview/<int:size>/<path:path>')
def get_file_preview(size, path):  # put application's code here
    abs_path = os.path.abspath(path)
    with open(abs_path) as file:
        result_text = file.read(size)
    return f"<b>{abs_path}</b> {len(result_text)}<br> {result_text}"


if __name__ == '__main__':
    app.run()

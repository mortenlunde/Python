from flask import Flask, request, render_template
import os
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', methods=['GET'])


@app.route('/submit', methods=['POST'])
def submit_data():
    name = request.form.get('name')
    age = request.form.get('alder')
    content = request.form.get('content')

    dato_b = datetime.now()
    dato_a = datetime.strftime(dato_b, '%Y-%m-%d-%M-%S')
    file_name = os.path.join(os.getcwd(), 'posted_data', f"{name}-{age}-{dato_a}'.txt")
    with open(file_name, "w+", encoding='utf-8') as send_data:
        send_data.write(f'{content}')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)

from flask import Flask, render_template, request, flash, jsonify
from lib.sql_code import fetch_database as sql_reader, sql_create_tasks, generate_random_tasks, fetch_task_sets

app = Flask(__name__)
app.secret_key = 'morten'


@app.route('/', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        task_name = request.form.get('task_name')
        num_tasks = request.form.get('num_tasks')

        result, num_tasks = sql_create_tasks(task_name, num_tasks)
        if result is not None:
            flash(result)

        result_generate = generate_random_tasks(result, int(num_tasks))
        if result_generate is not None:
            flash(result_generate)

    return render_template('index.html')


@app.route('/fetch_task_sets', methods=['GET', 'POST'])
def fetch_task_sets_route():
    if request.method == 'POST':
        task_sets = fetch_task_sets()
        return jsonify({'task_sets': task_sets})
    else:
        return jsonify({'error': 'Invalid request'})


@app.route('/view_tasks')
def view_database():
    tasks, header = sql_reader()
    return render_template('view_tasks.html', tasks=tasks, header=header)


if __name__ == '__main__':
    app.run(debug=True)
    app.secret_key = 'morten'

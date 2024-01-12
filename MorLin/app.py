from flask import Flask, render_template, request, jsonify, redirect
from lib.sql_queries import get_databases, get_tables, get_table_views, view_table_data

app = Flask(__name__)
chosendb = None
chosentable = None
chosenview = None


@app.route('/')
def fetch_databases():
    databases = get_databases()
    return render_template('index.html', databases=databases)


@app.route('/get_tables', methods=['POST'])
def fetch_tables():
    global chosendb
    if request.method == 'POST':
        chosendb = request.form['database']
        tables = get_tables(database=chosendb)
        return jsonify({'tables': tables})
    else:
        return jsonify({'error': 'Invalid request'})


@app.route('/fetch_table_view', methods=['POST'])
def fetch_table_view():
    global chosendb
    if request.method == 'POST':
        chosendb = request.form['database']
        views = get_table_views(database=chosendb)
        return jsonify({'tables': views})
    else:
        return jsonify({'error': 'Invalid request'})


@app.route('/show_table', methods=['GET'])
def show_table():
    global chosendb, chosentable, chosenview
    selected_table_or_view = request.args.get('table') or request.args.get('table_view')

    if selected_table_or_view:
        if request.args.get('table'):
            chosentable = selected_table_or_view
        elif request.args.get('table_view'):
            chosenview = selected_table_or_view

        data, headers = view_table_data(chosendb, selected_table_or_view)
        return render_template('view_data.html', data=data, headers=headers)
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=5000)

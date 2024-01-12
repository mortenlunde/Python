import json
from flask import Flask, render_template
import lib.person_data_reader as p_reader

app = Flask(__name__)


@app.route('/')
def show_person_data():
    person_list = []

    with open('persons.csv', "r", encoding="utf-8") as f:
        header = next(f).strip().split(',')
        for line in f:
            persons_arr = line.rstrip('\n').split(',')
            first_name, last_name, age, gender = persons_arr
            person_list.append((first_name, last_name, int(age), gender))

    return render_template('PersonData.html', persons=person_list, headers=header)


@app.route('/json')
def show_person_data_json():
    persons = p_reader.read_persons('persons.csv', True)
    person_list_json = [dict(zip(persons[0], p)) for p in persons[1:]]
    person_json = json.dumps(person_list_json)
    return render_template('PersonDataJSON.html', persons=json.loads(person_json))


if __name__ == '__main__':
    app.run(debug=True, port=8000)

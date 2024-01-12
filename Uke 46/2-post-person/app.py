from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    person_list = []
    with open('persons.csv', "r", encoding="utf-8") as f:
        header = next(f).strip().split(',')
        for idx, line in enumerate(f):
            persons_arr = line.rstrip('\n').split(',')

            if not len(persons_arr) == 4:
                print(f"Feil formot i filen: {idx+1} - {line}")
                continue

            first_name, last_name, age, gender = persons_arr

            if not all([first_name, last_name, age, gender]):
                print(f"Feil i data, mangler felter. Linjenummer {idx} - linje {line}")
                continue

            if not age.isdigit():
                print(f"Feil i alder- felt. Linjenummer {idx} - {line}")
                continue

            if not gender.lower() in ["mann", "kvinne"]:
                print(f"Feil i kjønn- feltet. Linjenummer {idx} - {line}")
                continue

            first_name, last_name, age, gender = persons_arr
            person_list.append((first_name, last_name, int(age), gender))

    return render_template('index.html', persons=person_list, headers=header)


@app.route('/add_person', methods=['GET', 'POST'])
def add_person():
    if request.method == 'POST':
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        age = request.form.get('alder')
        gender = request.form.get('gender')

        with open('persons.csv', "a", encoding="utf-8") as f:
            f.write(f"\n{first_name},{last_name},{age},{gender}")

        return redirect('/')  # Redirect to the home page after adding a person

    return render_template('add_person.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)

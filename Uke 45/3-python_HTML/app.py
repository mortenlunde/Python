from flask import Flask, render_template
import random as rnd

app = Flask(__name__)


@app.route('/')
def show_random_number():
    rnd_nr = rnd.randint(1, 20)
    return render_template('random_number.html',
                           my_random_number=rnd_nr,
                           numbers=[rnd.randint(1, 101) for _ in range(10)])


if __name__ == '__main__':
    app.run(debug=True)

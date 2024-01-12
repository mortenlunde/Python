from flask import Flask, render_template
import lib.sqlCode as sqlReader

app = Flask(__name__)


@app.route('/')
def show_nor_cities():
    byer, headers = sqlReader.import_nor_cities()
    return render_template('world.html', byer=byer, headers=headers)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

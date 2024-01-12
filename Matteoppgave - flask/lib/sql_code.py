import mysql.connector
import random as rnd


def fetch_database(task_set=None):
    try:
        if task_set:
            query = (f'SELECT Oppgave, Løsning FROM matteoppgaver.Oppgaver WHERE OppgaveSettID IN (SELECT OppgaveSettID'
                     f' FROM matteoppgaver.Oppgavesett WHERE Navn = %s)')
            params = (task_set,)
        else:
            query = 'SELECT Oppgave, Løsning FROM matteoppgaver.Oppgaver'
            params = None

        with mysql.connector.connect(host="localhost", port=3306, user="root",
                                     password="gokstad2023", database="matteoppgaver") as conn:

            with conn.cursor() as db_cursor:
                db_cursor.execute(query, params)
                tasks = db_cursor.fetchall()
                header = db_cursor.column_names

    except mysql.connector.DatabaseError as err:
        print(f"Error: {err}")

    return tasks, header


def sql_create_tasks(name, tasks):
    try:
        query = 'INSERT INTO matteoppgaver.Oppgavesett(Navn, AntallOppgaver) VALUES (%s, %s)'

        with mysql.connector.connect(host="localhost", port=3306, user="root",
                                     password="gokstad2023", database="matteoppgaver", autocommit=True) as conn:

            with conn.cursor() as db_cursor:
                db_cursor.execute(query, (name, tasks))
                oppgavesett_id = db_cursor.lastrowid

    except mysql.connector.DatabaseError as err:
        print(f"Error: {err}")

    return oppgavesett_id, tasks


def generate_random_tasks(task_set, nu_tasks):
    try:
        query = 'INSERT INTO matteoppgaver.Oppgaver(OppgaveSettID, Oppgave, Løsning) VALUES (%s, %s, %s)'

        with mysql.connector.connect(host="localhost", port=3306, user="root",
                                     password="gokstad2023", database="matteoppgaver", autocommit=True) as conn:

            with conn.cursor() as db_cursor:
                print("Inside generate_random_tasks")  # Debug print
                while nu_tasks:
                    nu_1 = rnd.randint(1, 100)
                    nu_2 = rnd.randint(1, 100)
                    rnd_task = create_task(nu_1, nu_2)
                    solution = calculate_result(rnd_task)
                    print(f"{nu_1},{nu_2} {rnd_task} {solution}")
                    db_cursor.execute(query, (task_set, rnd_task, solution))
                    nu_tasks -= 1

    except mysql.connector.DatabaseError as err:
        print(f"Error: {err}")

    return None


def fetch_task_sets():
    try:
        query = 'SELECT Navn FROM matteoppgaver.Oppgavesett'

        with mysql.connector.connect(host="localhost", port=3306, user="root",
                                     password="gokstad2023", database="matteoppgaver") as conn:

            with conn.cursor() as db_cursor:
                db_cursor.execute(query)
                task_sets = [row[0] for row in db_cursor.fetchall()]

    except mysql.connector.DatabaseError as err:
        print(f"Error: {err}")
        task_sets = []

    return task_sets


def create_task(x, y):
    operator = rnd.choice(['+', '-', '*', '/'])

    if operator == '+':
        return f"{x}+{y} = "
    elif operator == '-':
        return f"{x}-{y} = "
    elif operator == '*':
        return f"{x}*{y} = "
    elif operator == '/':
        while y == 0 or x % y != 0:
            x = rnd.randint(1, 100)
            y = rnd.randint(1, 100)
        return f"{x}/{y} = "


def calculate_result(expression):
    try:
        # Find the position of '=' in the expression
        equal_index = expression.find('=')
        if equal_index != -1:
            # Extract the part of the expression before '='
            expression_before_equal = expression[:equal_index].strip()

            # Evaluate the expression before '='
            result = eval(expression_before_equal)

            # Return the result
            return result
    except Exception as e:
        print(f"Error: {e}, Expression: {expression}")

    return None

import mysql.connector


def get_databases():
    databases = []
    try:
        query = "SHOW DATABASES"
        with mysql.connector.connect(host='localhost', port=3306, user='root',
                                     password='gokstad2023') as conn:
            with conn.cursor() as db_cursor:
                db_cursor.execute(query)
                databases = [database[0] for database in db_cursor.fetchall()]

    except mysql.connector.DatabaseError as err:
        print("Error", err)

    return databases


def get_tables(database):
    tables = []
    try:
        query = "SHOW TABLES"
        with mysql.connector.connect(host='localhost', port=3306, user='root',
                                     password='gokstad2023', database=f'{database}') as conn:
            with conn.cursor() as db_cursor:
                db_cursor.execute(query)
                tables = [table[0] for table in db_cursor.fetchall()]
    except mysql.connector.DatabaseError as err:
        print("Error", err)

    return tables


def get_table_views(database):
    table_views = []
    try:
        query = (f"SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_TYPE = 'VIEW' AND "
                 f"TABLE_SCHEMA = '{database}';")
        with mysql.connector.connect(host='localhost', port=3306, user='root',
                                     password='gokstad2023', database='information_schema') as conn:
            with conn.cursor() as db_cursor:
                db_cursor.execute(query)
                table_views = [view[0] for view in db_cursor.fetchall()]
    except mysql.connector.DatabaseError as err:
        print("Error", err)

    return table_views


def view_table_data(database, table):
    data = []
    headers = []
    try:
        query = f"SELECT * FROM {database}.{table}"
        with mysql.connector.connect(host='localhost', port=3306, user='root',
                                     password='gokstad2023', database=f'{database}') as conn:
            with conn.cursor() as db_cursor:
                db_cursor.execute(query)
                data = db_cursor.fetchall()
                headers = db_cursor.column_names

    except mysql.connector.Error as err:
        print("Error message:", err)

    return data, headers

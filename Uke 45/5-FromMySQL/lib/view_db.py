import mysql.connector


def import_nor_cities(chosen_db):
    try:
        query = f"SELECT * FROM {chosen_db}"

        with mysql.connector.connect(host='localhost', port=3306, user='root',
                                     password='gokstad2023', database=f'{chosen_db}') as conn:
            with conn.cursor() as db_cursor:
                db_cursor.execute(query)
                byer = db_cursor.fetchall()
                headers = db_cursor.column_names

    except mysql.connector.DatabaseError as err:
        print("Error", err)

    return byer, headers

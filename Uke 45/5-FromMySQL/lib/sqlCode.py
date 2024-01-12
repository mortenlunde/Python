import mysql.connector


def import_nor_cities():
    try:
        query = "SELECT * FROM world.city WHERE countrycode = 'NOR';"

        with mysql.connector.connect(host='localhost', port=3306, user='root',
                                     password='gokstad2023', database='world') as conn:
            with conn.cursor() as db_cursor:
                db_cursor.execute(query)
                byer = db_cursor.fetchall()
                headers = db_cursor.column_names

    except mysql.connector.DatabaseError as err:
        print("Error", err)

    return byer, headers

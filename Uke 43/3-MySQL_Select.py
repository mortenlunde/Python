import mysql.connector

try:
    query = "SELECT * FROM ncity WHERE countrycode = 'NOR';"

    with mysql.connector.connect(host='localhost', port=3306, user='root',
                                 password='gokstad2023', database='world') as conn:
        with conn.cursor() as db_cursor:
            db_cursor.execute(query)

            results = db_cursor.fetchall()
            for res in results:
                print(res)
except mysql.connector.DatabaseError as err:
    print("Error", res)

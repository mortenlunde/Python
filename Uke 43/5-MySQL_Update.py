import mysql.connector

try:
    pop = 1064235
    city = 'Oslo'
    query = """
                UPDATE ncity
                SET Population = %s
                WHERE Name like %s;
                """

    parameter_list = [pop, city]

    with mysql.connector.connect(host='localhost', port=3306, user='root',
                                 password='gokstad2023', database='world') as conn:
        with conn.cursor() as db_cursor:
            db_cursor.execute(query, parameter_list)

            if db_cursor.rowcount > 0:
                print("La til data i ncity- tabellen: ", parameter_list)
            else:
                print("Klarte ikke legge til data.")
        conn.commit()

except mysql.connector.DatabaseError as err:
    print("Error", err)

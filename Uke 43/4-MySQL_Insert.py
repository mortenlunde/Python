import mysql.connector

try:
    query = """
                INSERT INTO ncity(Name, CountryCode, Population)
                VALUES (%s, %s, %s);
                """

    parameter_list = ['Tønsberg', 'NOR', 54580]

    with mysql.connector.connect(host='localhost', port=3306, user='root',
                                 password='MoLuSa26i', database='world') as conn:
        with conn.cursor() as db_cursor:
            db_cursor.execute(query, parameter_list)

            if db_cursor.rowcount > 0:
                print("La til data i ncity- tabellen: ", parameter_list)
            else:
                print("Klarte ikke legge til data.")
        conn.commit()

except mysql.connector.DatabaseError as err:
    print("Error", err)

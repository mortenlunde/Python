import mysql.connector
import os

FILE = "byer.csv"


def read_cities(filename: str):
    if not os.path.exists(filename):
        return f"Filen '{filename}' eksisterer ikke."

    cities_list = []
    with open(filename, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):

            cities_arr = line.rstrip('\n').split(',')
            _city, pop = cities_arr

            cities_list.append((_city, int(pop)))

    return cities_list


cities_result = read_cities(FILE)

try:
    with mysql.connector.connect(host='localhost', port=3306, user='root',
                                 password='gokstad2023', database='world') as conn:
        with conn.cursor() as db_cursor:
            query = '''
                    INSERT INTO ncity (Name, CountryCode, Population)
                    VALUES (%s, 'NOR', %s)
                    '''
            for city, population in cities_result:
                try:
                    parameter_list = [city, population]
                    db_cursor.execute(query, parameter_list)
                    conn.commit()
                    print("Lagt til data i  ncity- tabellen:", parameter_list)
                except mysql.connector.IntegrityError as e:
                    print(f"Byen {city} finnes allerede. Hopper over.")
        conn.commit()

except mysql.connector.DatabaseError as err:
    print("Error", err)

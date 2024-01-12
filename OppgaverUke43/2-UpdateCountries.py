import mysql.connector
import os

FILE = "land.csv"


def read_countries(filename: str):
    if not os.path.exists(filename):
        return f"Filen '{filename}' eksisterer ikke."

    countries_list = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            countries_arr = line.rstrip('\n').split(',')
            _code, _country, pop = countries_arr
            try:
                _population = int(pop.strip())
                countries_list.append((_code, _country, _population))
            except ValueError:
                print(f"Ignored invalid population value: {pop} for country: {_country}")

    return countries_list


countries_result = read_countries(FILE)

try:
    with mysql.connector.connect(host='localhost', port=3306, user='root',
                                 password='MoLuSa26i', database='world') as conn:
        with conn.cursor() as db_cursor:
            for code, country, population in countries_result:
                db_cursor.execute('SELECT Code FROM ncountry WHERE Code = %s', (code,))
                existing_country = db_cursor.fetchone()

                if existing_country:
                    query = '''
                            UPDATE ncountry
                            SET Population = %s
                            WHERE Code = %s;
                            '''
                    db_cursor.execute(query, (population, code))
                    if db_cursor.rowcount > 0:
                        print(f"Oppdatert befolking for {country}")
                    else:
                        print(f"Ingen endring gjort for: {country}")
                else:
                    query = '''
                            INSERT INTO ncountry (Code, Name, Population)
                            VALUES (%s, %s, %s);
                            '''
                    db_cursor.execute(query, (code, country, population))
                    if db_cursor.rowcount > 0:
                        print(f"Lagt til {country}")
                    else:
                        print(f"Ingen endring gjort for: {country}")

                conn.commit()

except mysql.connector.DatabaseError as err:
    print("Error:", err)

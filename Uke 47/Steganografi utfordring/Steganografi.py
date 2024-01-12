import base64
import mysql.connector

#%% Konvertere txt til bildefil
filename = 'secret-bs64-jpg.txt'
filename_jpg = 'secret-bs64.jpg'

with open(filename, 'r') as read_data:
    file_content = read_data.read()
    file_content_bytes = file_content.encode('latin-1')
    decoded_bytes = base64.b64decode(file_content_bytes)

with open(filename_jpg, 'wb') as write_file:
    write_file.write(decoded_bytes)

#%% Oppggave 1
word = 'Programmering'
word_encode = word.encode('iso-8859-1')
oppgave_1 = sum(b for b in word_encode)
print(f"Oppgave 1: {oppgave_1}")


#%% Oppgave 2
def prime():
    prime_list = []
    while len(prime_list) < 7:
        for i in range(1, 100):
            if i == 0 or i == 1:
                continue
            else:
                for j in range(2, int(i/2)+1):
                    if i % j == 0:
                        break
                else:
                    prime_list.append(i)
    return prime_list


prime_7 = prime()[6]
chairs_fjorden = 82
oppgave_2 = prime_7 * chairs_fjorden
print(f"Oppgave 2: {oppgave_2}")

#%% Oppgave 3
oppgave_3 = 1991
print(f"Oppgave 4: {oppgave_3}")

#%% Oppgave 4
bnr_val = '11110110101'
oppgave_4 = int(bnr_val, 2)
print(f"Oppgave 4: {oppgave_4}")


#%% Oppgave 5
hex_val = '0xa16'
oppgave_5 = int(hex_val, 16)
print(f"Oppgave 5: {oppgave_5}")


#%% Oppgave 6
def sum_of_sevens():
    result = sum(range(0, 202, 7))
    return result


oppgave_6 = sum_of_sevens()
print(f"Oppgave 6: {oppgave_6}")


#%% Oppgave 7
try:
    query = '''SELECT DISTINCT products.productLine AS Productline, SUM(products.quantityInStock) AS Stock
               FROM products WHERE productLine = 'Motorcycles' '''
    with mysql.connector.connect(host='localhost', port=3306, user='root',
                                 password='gokstad2023', database='classicmodels') as conn:
        with conn.cursor() as db_cursor:
            db_cursor.execute(query)

            results = db_cursor.fetchall()
            for res in results:
                oppgave_7 = int(res[1])
except mysql.connector.DatabaseError as err:
    print("Error", res)

print(f"Oppgave 7: {oppgave_7}")

#%% Oppgave 8
try:
    query_2 = '''SELECT DISTINCT Name, cl.Language, SUM(Population) AS TotalPopulation
                 FROM world.country
                 JOIN world.countrylanguage cl ON Code = cl.CountryCode
                 WHERE Region = 'Southern Europe' AND cl.Language = 'English'
                 GROUP BY Name, cl.Language WITH ROLLUP '''

    with mysql.connector.connect(host='localhost', port=3306, user='root',
                                 password='gokstad2023', database='world') as conn:
        with conn.cursor() as db_cursor:
            db_cursor.execute(query_2)

            results = db_cursor.fetchall()
            for res in results:
                oppgave_8 = int(res[2])
except mysql.connector.DatabaseError as err:
    print("Error", res)

print(f"Oppgave 8: {oppgave_8}")


#%% SUM

with open('secret-bs64.jpg', 'rb') as read_bytes:
    file_bytes = read_bytes.read()

oppgaver = [oppgave_1, oppgave_2, oppgave_3, oppgave_4, oppgave_5, oppgave_6, oppgave_7, oppgave_8]

byte_values = [chr(file_bytes[pos]) for pos in oppgaver]

byte_values_str = ''.join(byte_values)
print(f"\nByte verdier av svarene: {byte_values_str}")

bts = bytes.fromhex(byte_values_str)
hemmelig_ord = bts.decode('utf-8')
print(f"Hemmelig ord: {hemmelig_ord}")

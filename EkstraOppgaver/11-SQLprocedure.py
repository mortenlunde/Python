import mysql.connector

try:
    query = '''CREATE PROCEDURE IF NOT EXISTS Stared(IN ChannelIDInput INT)
    BEGIN
        UPDATE Channel
        SET Stars = Stars + 1
        WHERE MeTubeStar = ChannelIDInput;
    END;'''

    with mysql.connector.connect(host='localhost', port=3306, user='root',
                                 password='gokstad2023', database='MeTube') as conn:
        with conn.cursor() as db_cursor:
            db_cursor.execute(query)
except mysql.connector.DatabaseError as err:
    print("Error", err)

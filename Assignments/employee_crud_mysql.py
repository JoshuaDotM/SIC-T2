import pymysql

def connect_db():
    connection = None
    try:
        connection = pymysql.connect(
            host="localhost", 
            user="root", 
            password="root@123", 
            database="JM_DB",  # Corrected spelling
            port=3306, 
            charset="utf8mb4"  # Using utf8mb4 for better Unicode support
        )
        print('Database Connected')
    except pymysql.MySQLError as e:
        print(f'Database Connection Failed: {e}')
    return connection

def disconnect_db(connection):
    try:
        connection.close()
        print('DB disconnected')
    except pymysql.MySQLError as e:
        print(f'DB disconnection failed: {e}')

def create_db():
    query = 'CREATE DATABASE IF NOT EXISTS nithin_db'
    connection = connect_db()  # Open the connection
    try:
        if connection:  # Check if connection was successful
            cursor = connection.cursor()
            cursor.execute(query)
            print('Database created')
            cursor.close()
    except pymysql.MySQLError as e:
        print(f'Database creation failed: {e}')
    finally:
        # Ensure that the DB connection is always closed, even if there's an error
        if connection:
            disconnect_db(connection)

# Main flow: create DB and disconnect after use
create_db()

import pymysql

def connectDb():
    connection = None
    try:
        # Correcting 'datebase' to 'database'
        connection = pymysql.connect(host="localhost", 
                                      user="root", 
                                      password="root@123", 
                                      database="JM_DB",  # Corrected spelling
                                      port=3306, 
                                      charset="utf8mb4")  # Using utf8mb4 for better Unicode support
        print('Database Connected')
    except pymysql.MySQLError as e:
        # More specific error handling
        print(f'Database Connection Failed: {e}')
    return connection

connection = connectDb()

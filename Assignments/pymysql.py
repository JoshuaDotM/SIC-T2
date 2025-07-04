import pymysql

def connect_to_mysql():
    # Connect without specifying database for initial DB creation check
    return pymysql.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

def create_database_if_not_exists(connection, db_name):
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`")
    connection.commit()

def use_database(connection, db_name):
    with connection.cursor() as cursor:
        cursor.execute(f"USE `{db_name}`")

def list_tables(connection):
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
    if tables:
        print("Available tables:")
        for t in tables:
            # 'SHOW TABLES' returns dict with key like 'Tables_in_databasename'
            print(list(t.values())[0])
    else:
        print("No tables found in this database.")

def create_table(connection):
    table_name = input("Enter new table name: ").strip()
    columns = input("Enter columns (e.g. id INT PRIMARY KEY, name VARCHAR(100)): ").strip()
    query = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({columns})"
    with connection.cursor() as cursor:
        try:
            cursor.execute(query)
            connection.commit()
            print(f"Table '{table_name}' created successfully.")
        except Exception as e:
            print(f"Error creating table: {e}")

def insert_into_table(connection):
    table = input("Enter table name to insert into: ").strip()
    with connection.cursor() as cursor:
        # Get columns from table to help user insert correct data
        cursor.execute(f"SHOW COLUMNS FROM `{table}`")
        columns_info = cursor.fetchall()
        if not columns_info:
            print("Table doesn't exist or has no columns.")
            return
        columns = [col['Field'] for col in columns_info]
        print("Table columns:", columns)

        values = []
        for col in columns:
            val = input(f"Enter value for '{col}': ")
            values.append(val)

        placeholders = ", ".join(["%s"] * len(columns))
        cols_formatted = ", ".join(f"`{col}`" for col in columns)
        insert_query = f"INSERT INTO `{table}` ({cols_formatted}) VALUES ({placeholders})"
        try:
            cursor.execute(insert_query, values)
            connection.commit()
            print("Row inserted successfully.")
        except Exception as e:
            connection.rollback()
            print(f"Insert failed: {e}")

def delete_from_table(connection):
    table = input("Enter table name to delete from: ").strip()
    condition = input("Enter condition to delete rows (e.g. id=3): ").strip()
    query = f"DELETE FROM `{table}` WHERE {condition}"
    with connection.cursor() as cursor:
        try:
            cursor.execute(query)
            connection.commit()
            print(f"{cursor.rowcount} row(s) deleted.")
        except Exception as e:
            connection.rollback()
            print(f"Delete failed: {e}")

def view_table(connection):
    table = input("Enter table name to view: ").strip()
    query = f"SELECT * FROM `{table}`"
    with connection.cursor() as cursor:
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print("No data in the table.")
        except Exception as e:
            print(f"Error fetching data: {e}")

def main():
    print("Connecting to MySQL server...")
    conn = connect_to_mysql()

    db_name = input("Enter database name to use or create: ").strip()
    create_database_if_not_exists(conn, db_name)
    use_database(conn, db_name)
    print(f"Using database `{db_name}`")

    while True:
        print("\nOptions:")
        print("1. List tables")
        print("2. Create a new table")
        print("3. Insert into a table")
        print("4. Delete from a table")
        print("5. View table data")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            list_tables(conn)
        elif choice == '2':
            create_table(conn)
        elif choice == '3':
            insert_into_table(conn)
        elif choice == '4':
            delete_from_table(conn)
        elif choice == '5':
            view_table(conn)
        elif choice == '6':
            print("Closing connection and exiting...")
            conn.close()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

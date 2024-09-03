def create_connection(db_file):
    import sqlite3
    from sqlite3 import Error
    print("DB connection entered")
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("DB connection live")
    except Error as e:
        print(f"Error: {e}")
    return conn


def close_connection(conn):
    """ closes a connection to a database """
    conn.close()


def select_all(conn):
    """select all rows from our table using the conn we already created """
    cur = conn.cursor()
    query = "select * from longley" # To-Do write the query to retrive all data from the longley table 
    cur.execute(query)

    rows = cur.fetchall()  # To-Do fetch all rows using the cursor cur

    return rows 


def print_rows(rows):
    """ Loop through the retrived rows of a table and print them"""
    # All of the function body is a todo task
    for row in rows:
        print(row)

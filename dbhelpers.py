# Woah so DRY! More helpers to keep my API endpoint code clean and free of repeated code.
# Don't forget to create your own dbcreds.py file!
import mariadb
import dbcreds
import traceback


def connect():
    # Create our connection and cursor to the DB and return them
    cursor, conn = None, None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,
                               host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
    except:
        print("Error connecting to DB!")
        traceback.print_exc()
    return conn, cursor


def disconnect(conn, cursor):
    # Close the passed in cursor
    try:
        cursor.close()
    except:
        print("Issue closing cursor")
        traceback.print_exc()
    try:
        conn.close()
    except:
        print("Issue closing connection")
        traceback.print_exc()


# The same comments apply to all the helper functions in here!
def run_select_statement(sql, params):
    # Do the normal open and variable setup
    conn, cursor = connect()
    result = None

    # Try to run the command based on the SQL and params passed in
    try:
        cursor.execute(sql, params)
        result = cursor.fetchall()
    # TODO Do a better job of catching more specific errors! Might need to find a way to return error-specific results
    except:
        traceback.print_exc()
        print("DO BETTER ERROR CATCHING")

    # Close the resources
    disconnect(conn, cursor)
    # Return the result
    return result


def run_insert_statement(sql, params):
    conn, cursor = connect()
    result = None

    try:
        cursor.execute(sql, params)
        conn.commit()
        # In this example we always return the lastrowid for an INSERT
        # This might not always be what you need / want
        result = cursor.lastrowid
    except:
        traceback.print_exc()
        print("DO BETTER ERROR CATCHING")

    disconnect(conn, cursor)
    return result


def run_delete_statement(sql, params):
    conn, cursor = connect()
    result = None

    try:
        cursor.execute(sql, params)
        conn.commit()
        # In this example we always return the rowcount for an DELETE
        # This might not always be what you need / want
        result = cursor.rowcount
    except:
        traceback.print_exc()
        print("DO BETTER ERROR CATCHING")

    disconnect(conn, cursor)
    return result


def run_update_statement(sql, params):
    conn, cursor = connect()
    result = None

    try:
        cursor.execute(sql, params)
        conn.commit()
        # In this example we always return the rowcount for an UPDATE
        # This might not always be what you need / want
        result = cursor.rowcount
    except:
        traceback.print_exc()
        print("DO BETTER ERROR CATCHING")

    disconnect(conn, cursor)
    return result

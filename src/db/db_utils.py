import sqlite3

def connect():
    connection = None
    try:
        connection = sqlite3.connect('assets.sqlite')
    except sqlite3.error as e:
        print(e)
    return connection

def exec_get_one(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    one = cur.fetchone()
    conn.close()
    return one

def exec_get_all(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    list_of_tuples = cur.fetchall()
    conn.close()
    return list_of_tuples

def exec_commit(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    conn.commit()
    conn.close()
    return result

def exec_insert_returning(sql, args={}):
    """
    Execute the SQL statement, commits the change, and returns the primary key created.
    Intended for data changes, not queries.
    If you DON'T need the primary key or some other RETURNING clause,
        use exec_commit instead.
    
    Parameters:
        sql - string of SQL to execute
        args - dictionary of named parameters for sqlite3's
                prepared statements
    
    Example:
        # Count the number of rows where "foo" is "baz"
        id = exec_insert_returning("INSERT INTO mytable(user, email) VALUES (? , ?)",
                    {'userfoo': 'john', 'emailfoo': 'john.doe@example.com'})
        # id has the primary key of the new record
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    sqlite_returning = cur.lastrowid
    conn.commit()
    conn.close()
    return sqlite_returning
import sqlite3

def initialize_sqlite_db():
    connection = sqlite3.connect("assets.sqlite")

    cursor = connection.cursor()

    sql_drop_query = """
        DROP TABLE IF EXISTS CYBER_ASSET;
    """

    sql_create_query = """ 
        CREATE TABLE CYBER_ASSET (
        ID INTEGER PRIMARY KEY,
        NAME VARCHAR(256) NOT NULL,
        TYPE VARCHAR(50) NOT NULL,
        SERIAL_NUMBER VARCHAR(50) NOT NULL,
        OPERATING_SYSTEM VARCHAR(15) NOT NULL
        )   
    """

    cursor.execute(sql_drop_query)
    cursor.execute(sql_create_query)
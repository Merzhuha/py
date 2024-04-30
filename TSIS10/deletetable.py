import psycopg2
from smart import host, user, password, dbname
connection=None

try:
    #connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=dbname,
        client_encoding="utf-8"
    )
    connection.autocommit=True
    
    # delete a table
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE phonebook;"""
        )
        
        print("[INFO] Table was deleted")



except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")

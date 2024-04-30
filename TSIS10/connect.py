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

    #the curser for performing database operations
    #cursor=connection.cursor()
    
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
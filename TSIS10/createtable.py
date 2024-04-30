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

    #create a new table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE phonebook(
            phone_numb VARCHAR(12) NOT NULL,
            user_name VARCHAR(50) NOT NULL);"""
        )
        #connection.commit()
        print("[INFO] Table created succesfully")
        
    
    '''#insert data into a table
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO phonebook(phone_number, username) 
            VALUES ('87054758500', 'Barbarossa');
            INSERT INTO phonebook(phone_number, username) 
            VALUES ("f{phone}", name);"""
        )
        
        print("[INFO] Data was succesfully inserted")
    
    # delete a table
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE phonebook;"""
        )
        
        print("[INFO] Table was deleted")'''



except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")


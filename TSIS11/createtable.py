import psycopg2
from smart import host, user, password, dbname
import csv
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
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")

commands = [
	"""
	CREATE TABLE accounts(
		user_name VARCHAR (20) UNIQUE NOT NULL,
		phone_numb VARCHAR (20) UNIQUE NOT NULL
	);
	"""	,
	#TASK 2
	"""
	CREATE OR REPLACE PROCEDURE add_user(name varchar, num varchar)
		as 
		$$
		BEGIN
		insert into accounts(user_name, phone_numb)
		values(name, num);
		END; 
		$$
		LANGUAGE plpgsql;
	""",
	"""
		CREATE OR REPLACE PROCEDURE add_user1(name varchar, num varchar)
		as 
		$$
		BEGIN
		update accounts
			set phone_numb  = $2
			where accounts.user_name = name ;
		END; 
		$$
		LANGUAGE plpgsql;
	""",
	#TASK 4
	"""
	CREATE OR REPLACE FUNCTION que(lim integer, x integer)
		returns setof accounts
		as
		$$
		BEGIN
			return query
			select * from accounts
			order by user_name
			limit lim offset x;
		END;
		$$
		LANGUAGE plpgsql;
	""",
	#TASK 5
	"""
	CREATE OR REPLACE PROCEDURE del(name varchar)
        as
        $$
        BEGIN
        	delete
            from  accounts
            where accounts.user_name = name;
        END;
        $$
        LANGUAGE plpgsql;
	""",
	"""
	CREATE OR REPLACE PROCEDURE del1(num varchar)
        as
        $$
        BEGIN
        	delete
            from  accounts
            where accounts.phone_numb = num;
        END;
        $$
        LANGUAGE plpgsql;
	""",
	#TASK 1
	"""
	CREATE OR REPLACE FUNCTION show()
		returns table(
			user_name varchar(255),
		    phone_numb varchar(255)
		)
		as
		$$
		BEGIN 
		  return query
		  select s.user_name, s.phone_numb from accounts as s;
		END
		$$ 
		LANGUAGE plpgsql;
	"""
]

connection = None
try:
	params = {
    'host': host,
    'user': user,
    'password': password,
    'database': dbname,
    'client_encoding': 'utf-8'
}
	connection = psycopg2.connect(**params)
	cur = connection.cursor()
	for i in commands:
		cur.execute(i)
	cur.close()
	connection.commit()
except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex)
if connection is not None:
	connection.close()
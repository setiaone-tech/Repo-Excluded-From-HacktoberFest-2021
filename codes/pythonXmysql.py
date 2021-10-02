#################################
## Connect python with mysql
## Requirements: 
## Install MySql workbench: https://dev.mysql.com/downloads/workbench/
## create a database/schema called "test"
## Run this script to connect to that mysql server
#################################
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password= getpass("Enter password: "),
        ## TODO: your database name that you created in mysql work bench
        database = "test"
    ) as connection:
        print(connection)

        with connection.cursor() as cursor:
            cursor.execute("SELECT database();")
            record = cursor.fetchone()
            print("Your are connected to database: ", record)
            
            
            table_name = 'my_first_table'
            print("Creating table")
            cursor.execute(f'DROP TABLE IF EXISTS {table_name};')
            # print("i got here")
            cursor.execute(f'CREATE TABLE {table_name} (id INT PRIMARY KEY, num_races INT,\
                                                                venue_1 DECIMAL(5,2),venue_2 DECIMAL(5,2),venue_3 DECIMAL(5,2),venue_4 DECIMAL(5,2),venue_5 DECIMAL(5,2),venue_6 DECIMAL(5,2));')
            print("Table is created.....")


            connection.commit()
except Error as e:
    print(e)
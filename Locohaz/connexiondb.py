from getpass import getpass
import _mysql_connector
from MySQLdb import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        create_query = "CREATE DATABASE locohaz"
        with connection.cursor() as cursor:
            cursor.execute(create_query)

        print(connection)
except Error as e:
    print(e)





import sqlite3
from Employee import Employee

# Help: 
    # https://www.tutorialspoint.com/sqlite/sqlite_overview.htm
    # https://www.sqlite.org/lang_corefunc.html

Connection = sqlite3.connect("employee.db")

Cursor = Connection.cursor() # Allows you to execute queries to communicate with the MySQL database.

# Cursor.execute(""" CREATE TABLE Table_Name (
#     Column 1 int(6) UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT, /* First will be your Primary key */
#     Column 2 varchar(x), /* Next will be attributes about the entity */
#     Column 3 int(6), FOREIGN KEY (Foreign_Key_Name) REFERENCES Table_Name(Attribute_Name) 
#     )""")


# Cursor.execute("""CREATE TABLE employees (
#              first text,
#              last text,
#              pay integer
#              )""")


# Employee Objects
emp_1 = Employee("John", "Doe", 80000)
emp_2 = Employee("Jane", "Doe", 90000)

# Connection.commit()

"""
Querying
The fetchall() method retrieves all the rows in the result set of a query and returns them as list of tuples. (If we execute this after retrieving few rows it returns the remaining ones).
The fetchone() method fetches the next row in the result of a query and returns it as a tuple.
The fetchmany() method is similar to the fetchone() but, it retrieves the next set of rows in the result set of a query, instead of a single row.

# Cursor.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {"first":emp_2.first, "last":emp_2.last, "pay":emp_2.pay })

"""

def query(TableName, Attribute, Who):
    Cursor.execute(f"SELECT * FROM {TableName} WHERE {Attribute}=?", (f"{Who}",))
    return Cursor.fetchall() 
    Connection.commit() #Commit your changes in the database

print(query("employees", "first", "Jessica")[0][2])


Connection.commit() 
Connection.close() #Closing the connection
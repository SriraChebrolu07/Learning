import os
import mysql.connector
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
#import streamlit as st

#Establish a connection to MySQL Server


mydb = mysql.connector.connect(
     host=os.getenv("MYSQL_HOST", "localhost"),
     user=os.getenv("MYSQL_USER", "root"),
     password=os.getenv("MYSQL_PASSWORD", ""),
     database=os.getenv("MYSQL_DATABASE", "sriram1"),
    )
mycursor=mydb.cursor()
print("Connection Established")

#df=pd.read_sql("select * from students2",mydb)

#print(df)

#  Create a new table

# def create():
#  create_table_query = """
#  CREATE TABLE students2 (
#     id INT PRIMARY KEY,
#     name VARCHAR(30),
#     age INT,
#     grade VARCHAR(10)
#  )
#  """
#  mycursor.execute(create_table_query)
#  mydb.commit()
#  print("New table 'students2' created successfully")


# create()

# def insert():
#         insert_query = "INSERT INTO students2 (id, name, age, grade) VALUES (%s, %s, %s, %s)"
#         data = [
#             (1, 'ram', 21, '9'),
#             (2, 'sam', 22, '9'),
#             (3, 'suresh', 21, '9')
#         ]
#         mycursor.executemany(insert_query, data)
#         mydb.commit()
#         print("Data inserted into 'students2' table successfully")
    

# insert()


# def update():
#     column = input("Enter the name of the column to update:\n ")
#     new_value = input("Enter the new value:\n ")
#     condition_column = input("Enter the name of the column for the condition:\n ")
#     condition_value = input("Enter the value for the condition:\n ")

#     update_query = f"UPDATE students2 SET {column} = %s WHERE {condition_column} = %s"
#     update_data = (new_value, condition_value)
#     mycursor.execute(update_query, update_data)
#     mydb.commit()
#     print(f"{mycursor.rowcount} row(s) updated successfully")

# update()




def delete_row(condition_column, condition_value):

        delete_query = f"DELETE FROM students2 WHERE {condition_column} = %s"
        delete_data = (condition_value,)
        mycursor.execute(delete_query, delete_data)
        mydb.commit()
        print(f"{mycursor.rowcount} row(s) deleted successfully")
        return mycursor.rowcount



delete_row("name","suresh")


def create_view():
    """
    Create a view for the 'students2' table.
    """
    try:
        view_query = """
        CREATE VIEW students_view AS
        SELECT * FROM students2
        """
        mycursor.execute(view_query)
        print("View 'students_view' created successfully")
    except mysql.connector.Error as err:
        print(f"Error creating view: {err}")

def fetch_view_data():
    
    
    mycursor.execute("SELECT * FROM students_view")
    result = mycursor.fetchall()
    if result:
            for row in result:
                print(row)
    else:
            print("No data found in the view")

# Example usage:
create_view()
fetch_view_data()

# # Close the connection
# mycursor.close()
# mydb.close()
# print("Connection closed")

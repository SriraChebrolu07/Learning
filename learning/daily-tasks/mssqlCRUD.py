import pyodbc
import pandas as pd



conn_str = ("Driver={ODBC Driver 17 for SQL Server};"

            "Server=SRIRAMCHEBROLU;"

            "Database=sriram;"

            "Trusted_Connection=yes;")

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
print("connection established successfully")
#acursor.execute("Select * from dummy")

df=pd.read_sql("select * from users",conn)

print(df)

 
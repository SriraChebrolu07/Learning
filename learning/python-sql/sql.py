# import pyodbc
# import pandas as pd

# conn_str = (
#     "Driver={ODBC Driver 17 for SQL Server};"
#     "Server=SRIRAMCHEBROLU;"
#     "Database=sql main;"
#     "Trusted_Connection=yes;"
# )

# conn = pyodbc.connect(conn_str)
# print("connection established")
# cursor = conn.cursor()

# cursor.execute("SELECT * FROM sales")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)  





# import pandas as pd
# import pyodbc

#  # Database connection details
# conn_str = ("Driver={ODBC Driver 17 for SQL Server};"

#             "Server=SRIRAMCHEBROLU;"

#             "Database=sql main;"

#             "Trusted_Connection=yes;")

# conn = pyodbc.connect(conn_str)
# cursor = conn.cursor()

# # cursor.execute("Select * from dummy")

# df=pd.read_sql("select * from test",conn)

# print(df)










import pandas as pd
import pyodbc

# Database connection details
conn_str = ("Driver={ODBC Driver 17 for SQL Server};"
            "Server=SRIRAMCHEBROLU;"
            "Database=sql main;"
            "Trusted_Connection=yes;")

# Table name to insert data
table_name = 'mytest'

# Establish a connection to SQL Server
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Drop existing table if it exists
drop_table_query = f'DROP TABLE IF EXISTS {table_name}'
cursor.execute(drop_table_query)
conn.commit()

# Define your create table query here
create_table_query = f'CREATE TABLE {table_name} (column1 INT, column2 VARCHAR(50),column3 INT)'  # Adjust column names and types as needed

# Execute the CREATE TABLE query
cursor.execute(create_table_query)
conn.commit()

# Read the CSV file into a pandas DataFrame
try:
    df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print(f"Error: CSV file '{csv_file_path}' not found.")
    conn.close()
    exit(1)

# Insert data into the table
for index, row in df.iterrows():
    insert_query = f'INSERT INTO {table_name} VALUES ({",".join(["?" for _ in row])})'
    cursor.execute(insert_query, tuple(row))
    conn.commit()

print("Data imported successfully")

# Close the connection
conn.close()

print("Table created successfully")

# Close the connection
conn.close()

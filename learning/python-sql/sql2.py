# import pyodbc
# import pandas as pd
# # Database connection details
# conn_str = ("Driver={ODBC Driver 17 for SQL Server};"
#             "Server=SRIRAMCHEBROLU;"
#             "Database=sql main;"
#             "Trusted_Connection=yes;")

# create_table_query = """
#                     CREATE TABLE mytest (
#                         Id INT PRIMARY KEY,
#                         Name VARCHAR(25),
#                         Age INT
#                     );
#                     """

# conn = pyodbc.connect(conn_str)
# cursor = conn.cursor()

# cursor.execute(create_table_query)


# conn.commit()
# print("table created successfully")


# cursor.close()
# conn.close()



import pyodbc
import pandas as pd

# Database connection details
conn_str = ("Driver={ODBC Driver 17 for SQL Server};"
            "Server=SRIRAMCHEBROLU;"
            "Database=sql main;"
            "Trusted_Connection=yes;")

create_table_query = """
                    CREATE TABLE mytest (
                        Id INT PRIMARY KEY,
                        Name VARCHAR(25),
                        Age INT
                    );
                    """

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

cursor.execute(create_table_query)

# Path to your CSV file
csv_file_path = 'test.csv'

# Table name to insert data
table_name = 'mytest'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Iterate over rows in the DataFrame and insert them into the SQL Server table
for index, row in df.iterrows():
    cursor.execute("INSERT INTO {} (Id, Name, Age) VALUES (?, ?, ?);".format(table_name), row['Id'], row['Name'], row['Age'])


conn.commit()
print("Data inserted successfully.")


cursor.close()
conn.close()

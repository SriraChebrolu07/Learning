import pyodbc

conn_str = 'DRIVER={SQL Server};SERVER=SRIRAMCHEBROLU;DATABASE=sql main;Trusted_Connection=yes;'

try:
    connection = pyodbc.connect(conn_str)
    print('Connected to SQL Server')

    cursor = connection.cursor()
    insertquery = "insert into cars(Serial_no,brand,price) values (?,?,?)"

    cursor.execute(insertquery, (4, 'toyota', 2100000))
    connection.commit()
    print("Data inserted successfully!")
except Exception as e:
    print(f'Error: {str(e)}')
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()

import pyodbc

conn_str = 'DRIVER={SQL Server};SERVER=SRIRAMCHEBROLU;DATABASE=sql main;Trusted_Connection=yes;'

try:
    connection = pyodbc.connect(conn_str)
    print('Connected to SQL Server')

    cursor = connection.cursor()
    query = 'SELECT * FROM cars'

    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as e:
    print(f'Error: {str(e)}')
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()

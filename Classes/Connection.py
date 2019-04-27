import pymysql.cursors
import pyodbc
from Classes import DbRequests

class Connection():


    def __init__(self):
            # Call the parent class constructor
            super().__init__()

    def Open_connection_MySQL(self):       
        dbquery = DbRequests.DbRequests()
        connection = pymysql.connect (host = "localhost",
                                      user = "root",
                                      passwd = "1234",
                                      db = "ocpizza")

        cursor = connection.cursor()
        cursor.execute ("SELECT VERSION()")
        dbquery.Insert_stores(cursor)
        row = cursor.fetchone()
        print("server version:", row[0])
        connection.commit()
        cursor.close()
        connection.close()
        return connection 

# Connection to SQL server
    def Open_connection_SQLServer(self):
        dbquery = DbRequests.DbRequests()
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=JOTA\\SQLEXPRESS;'
                              'Database=OCPIZZA;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM OCPIZZA.dbo.Aliment')
        dbquery.Create_DB(cursor)
        for row in cursor:
            print(row)

        return conn
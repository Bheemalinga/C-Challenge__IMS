import pyodbc # useful for connecting to SQL Server
from util.PropertyUtil import PropertyUtil

class DBConnection :
    connection = None

    @staticmethod
    def getConnection() :
        if DBConnection.connection is None :
            try:
                Credentials = PropertyUtil.getPropertyString()
                DBConnection.connection = pyodbc.connect(Credentials)
                print("\n\tPython and DB handshake successful.")
            except Exception as e :
                print(f"Python-DB Handshake failed : {e}")
        return DBConnection.connection
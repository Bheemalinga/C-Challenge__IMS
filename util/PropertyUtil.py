"""
 Create a utility class DBConnection in a package util with a static variable connection of Type
Connection and a static method getConnection() which returns connection.
Connection properties supplied in the connection string should be read from a property file.
Create a utility class PropertyUtil which contains a static method named getPropertyString() which
reads a property fie containing connection details like hostname, dbname, username, password, port
number and returns a connection string.
"""

class PropertyUtil:
    @staticmethod
    def getPropertyString():
        return (
            'Driver={SQL Server};'
            'Server=BMA-DESKTOP-K4C\\SQLEXPRESS;'
            'Database=Insurance_Management_System;'
            'Trusted_Connection=yes;'
        )
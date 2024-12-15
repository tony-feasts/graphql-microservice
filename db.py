import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="cloudproject.crimg8c22499.us-east-2.rds.amazonaws.com",
        user="admin",
        password="",
        database="welcomeStatistics"
    )
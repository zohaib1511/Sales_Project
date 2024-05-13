import os 
from dotenv import load_dotenv
import mysql.connector 
import pandas as pd


load_dotenv()

host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
database = 'swiftmarket'

connector = mysql.connector.connect(host=host,
                                   user=user,
                                   password=password,
                                   database=database)

cursor = connector.cursor()

def read_query(query):
    cursor.execute(query)
    rows=cursor.fetchall()
    df=pd.DataFrame(data=rows,columns=cursor.column_names)

    return df

def show_tables():
    query = """SHOW TABLES;"""
    cursor.execute(query)
    rows=cursor.fetchall()
    df=pd.DataFrame(data=rows,columns=cursor.column_names)


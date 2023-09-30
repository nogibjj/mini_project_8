'''
Query the database
'''
import sqlite3

def query():
    conn = sqlite3.connect("real_2016_air.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM real_2016_air LIMIT 10")
    print("Top 10 rows of real_2016_air table:")
    print(cursor.fetchall())
    conn.close()
    return "Success" 
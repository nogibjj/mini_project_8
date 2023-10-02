"""
Query the database
"""
import sqlite3


def querycreate():
    conn = sqlite3.connect("rainfall.db")
    cursor = conn.cursor()
    # create execution
    cursor.execute(
        "INSERT INTO rainfall (Date,POONDI,CHOLAVARAM,REDHILLS,CHEMBARAMBAKKAM) VALUES(31-12-2003,1,1,1,1)"
    )
    conn.close()
    return "Create Success"


def queryRead():
    conn = sqlite3.connect("rainfall.db")
    cursor = conn.cursor()
    # read execution
    cursor.execute("SELECT * FROM rainfall LIMIT 10")
    conn.close()
    return "Read Success"


def queryUpdate():
    conn = sqlite3.connect("rainfall.db")
    cursor = conn.cursor()
    # update execution
    cursor.execute("UPDATE rainfall SET POONDI = 1 WHERE id = 1 ")
    conn.close()
    return "Update Success"


def queryDelete():
    conn = sqlite3.connect("rainfall.db")
    cursor = conn.cursor()
    # delete execution
    cursor.execute("DELETE FROM rainfall WHERE id = 3")
    conn.close()
    return "Delete Success"


if __name__ == "__main__":
    querycreate()
    queryRead()
    queryUpdate()
    queryDelete()

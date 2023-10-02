"""
Transforms and loads data to local SQlite3 database
"""
import sqlite3
import csv
import os


def load(dataset="../data/rainfall.csv"):
    # print the full working directory
    # print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("rainfall.db")
    c = conn.cursor()
    # create new table for the database rainfall
    c.execute("DROP TABLE IF EXISTS rainfall")
    c.execute(
        """
              CREATE TABLE rainfall (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              Date DATE,
              POONDI FLOAT,
              CHOLAVARAM FLOAT,
              REDHILLS FLOAT,
              CHEMBARAMBAKKAM FLAOT)
              """
    )
    # insert values
    c.executemany(
        """
                  INSERT INTO rainfall 
                  (Date,POONDI,CHOLAVARAM,REDHILLS,CHEMBARAMBAKKAM)
                  VALUES(?,?,?,?,?)
                  """,
        payload,
    )
    conn.commit()
    conn.close()
    return "rainfall.db"


if __name__ == "__main__":
    load()

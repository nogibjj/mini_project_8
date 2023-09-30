'''
Transforms and loads data to local SQlite3 database
'''
import sqlite3
import csv
import os

dataset = "/workspace/mini_project_5/data/real_2016_air.csv"
# load csv file and insert into a sqlite3 database
def load(dataset = "/workspace/mini_project_5/data/real_2016_air.csv"):

    # print the full working directory
    print(os.getcwd())
    payload = csv.reader(open(dataset,newline=""),delimiter=",")
    conn = sqlite3.connect("real_2016_air.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS real_2016_air")
    c.execute("CREATE TABLE real_2016_air (id,T,TM,Tm,SLP,H,VV,V,VM,PM 2.5)")
    # insert values
    c.executemany("INSERT INTO real_2016_air VALUES(?,?,?,?,?,?,?,?,?,?)",payload)
    conn.commit()
    conn.close()
    return "real_2016_air.db"

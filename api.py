import psycopg2 as psql
import os, time, datetime, re, mimetypes, traceback, base64

conn = psql.connect("dbname=anuario user=postgres")
c = conn.cursor()

def create_user(username, email, password):
    pass

def insert(data):
    cols = []
    vals = []
    for cv in data.items():
        cols.append(cv[0])
        vals.append(cv[1])
    query = "INSERT INTO %s () VALUES ()"
    cur.execute(query, values)
    pass

cur.close()
conn.close()

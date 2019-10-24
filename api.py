import psycopg2 as psql
import os, time, datetime, re, mimetypes, traceback, base64

conn = psql.connect("dbname=anuario user=postgres")
c = conn.cursor()

def create_user(username, email, password):
    pass

def placeholders(list_of_items):
    s = []
    s += ["%s" for _ in list_of_items]
    return ",".join(s)

def value_lists(data):
    cols = []
    vals = []
    for cv in data.items():
        cols.append(cv[0])
        vals.append(cv[1])
    return cols, vals

def insert(data):
    cols, vals = value_lists(data)
    query f"INSERT INTO %s ({sput(cols)}) VALUES ({sput(vals)})"
    values = tuple(cols + vals)
    cur.execute(query, values)
    pass

cur.close()
conn.close()

import psycopg2 as psql
import os, time, datetime, re, mimetypes, traceback, base64

conn = psql.connect("dbname=anuario user=postgres")
c = conn.cursor()

def create_user(username, email, password):
    pass

cur.close()
conn.close()

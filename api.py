import psycopg2 as psql
from hashlib import sha512
from traceback import print_exc
from base64 import b64encode
from random import randint

def connect(password=None):
    conn = psql.connect(f"dbname=anuario user=postgres password={password}")
    del password
    c = conn.cursor()
    return conn, c

def hash_string(string):
    for _ in range(50000):
        string = sha512(string.encode()).hexdigest()
    return string

def latest_idn(password=None) -> int:
    conn, c = connect(password)
    c.execute("SELECT curnum FROM base.id_origins ORDER BY curnum DESC")
    last_num = c.fetchone()[0]
    new_num = last_num + randint(1, 20)
    c.close()
    conn.close()
    return new_num

def new_uid(limit: int, password=None) -> str:
    conn, c = connect(password)
    new_num = latest_idn()
    c.execute("INSERT INTO base.id_origins (curnum) VALUES (%s)", (new_num,))
    hashed = hash_string(str(new_num))
    c.close()
    conn.close()
    return hashed[:limit]

def sput(items: tuple) -> str:
    """Function that accepts a tuple and
    turns it into a string of \%s's for
    psycopg2 query formatting."""
    s = ["%s" for _ in items]
    return ",".join(s)

def value_tuples(data: dict) -> tuple:
    """Function that accepts a dictionary
    of values and returns two tuples, one
    for the keys and one for the values."""
    table = data['table']
    data.pop('table')
    cols = []
    vals = []
    for cv in data.items():
        cols.append(cv[0])
        vals.append(cv[1])
    return table, tuple(cols), tuple(vals)

def get_picture(path):
    with open(path, 'rb') as pict:
        return pict.read()

def tuple_to_no_quote_str(tup: tuple) -> str:
     return str(tup).replace("'", "")

def insert(data: dict, rest: str="", password=None) -> bool:
    conn, c = connect(password)
    """Function that accepts a data dictionary and
    inserts the values into a database, using the
    "table" field as the table and the "rest" field
    as an addition to the normal insert clause.
    Example use:
        insert({
            "table": "tablename",
            "uid": new_uid(25),
            "asst_text": "a second picture!",
            "pict": get_picture("example.png")
        })"""
    try:
        table, cols, vals = value_tuples(data)
        query = f"INSERT INTO {table} {tuple_to_no_quote_str(cols)} VALUES ({sput(vals)})"
        if rest != "":
            query += " " + rest
        print(cols, vals[:-1])
        c.execute(query, vals)
        conn.commit()
        c.close()
        conn.close()
        return True
    except:
        print_exc()
        c.close()
        conn.close()
        return False

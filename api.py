import psycopg2 as psql
from hashlib import sha512
from traceback import print_exc
from base64 import b64encode
from random import randint

while True:
    password = input("Senha de 'postgres'> ")
    try:
        conn = psql.connect(f"dbname=anuario user=postgres password={password}")
        del password
    except:
        break
c = conn.cursor()

def hash_string(string):
    for _ in range(50000):
        string = sha512(string.encode()).hexdigest()
    return string

def latest_idn() -> int:
    c.execute("SELECT curnum FROM id_origins ORDER BY curnum DESC")
    last_num = c.fetchone()[0]
    new_num = last_num + randint(1, 20)
    return new_num

def new_uid(limit: int) -> str:
    new_num = latest_idn()
    c.execute("INSERT INTO id_origins (curnum) VALUES %s", (new_num,))
    hashed = hash_string(str(new_num))

def create_user(username: str, email: str, password: str) -> bool:
    uid = ""
    try:
        return insert({
            "uid": new_uid()
            "username": username,
            "email": email,
            "password", hash_password(password)
        })
    except:
        print_exc();
        return False

def placeholders(items: list) -> str:
    s = []
    s += ["%s" for _ in items]
    return ",".join(s)

def value_tuples(data: dict) -> tuple:
    ''' Function that accepts a dictionary
    of values and returns two tuples, one
    for the keys and one for the values '''
    table = data['table']
    data.pop('table')
    cols = []
    vals = []
    for cv in data.items():
        cols.append(cv[0])
        vals.append(cv[1])
    return table, tuple(cols), tuple(vals)

def insert(data: dict, rest: str="") -> bool:
    '''Functon that accepts a data dictionary and
    inserts the values into a database, using the
    "table" field as the table and the "rest" field
    as an addition to the normal insert clause. '''
    try:
        table, cols, vals = value_tuples(data)
        query = f"INSERT INTO %s ({sput(cols)}) VALUES ({sput(vals)})"
        values = (table,) + cols + vals
        if rest != "":
            query += " " + rest
        cur.execute(query, values)
        conn.commit()
        return True
    except:
        print_exc()
        return False

cur.close()
conn.close()

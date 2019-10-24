import psycopg2 as psql
import traceback, base64

while True:
    password = input("Senha de 'postgres'> ")
    try:
        conn = psql.connect(f"dbname=anuario user=postgres password={password}")
        del password
    except:
        break
c = conn.cursor()

def create_user(username, email, password):
    pass

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
    return tuple(cols), tuple(vals)

def insert(data):
    try:
        cols, vals = value_tuples(data)
        value_tuples()
        query = f"INSERT INTO %s ({sput(cols)}) VALUES ({sput(vals)})"
        values = cols + vals
        cur.execute(query, values)
        conn.commit()
    except:
        traceback.print_exception()

cur.close()
conn.close()

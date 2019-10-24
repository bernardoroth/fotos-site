import psycopg2 as psql
import traceback, base64

while password := input("Senha de 'postgres'> "):
    if password.replace(" ", "") != "":
        conn = psql.connect(f"dbname=anuario user=postgres password={password}")
c = conn.cursor()

def create_user(username, email, password):
    pass

def placeholders(list_of_items):
    s = []
    s += ["%s" for _ in list_of_items]
    return ",".join(s)

def value_lists(data: dict) -> void:
    table = data['table']
    data.pop('table')
    cols = []
    vals = []
    for cv in data.items():
        cols.append(cv[0])
        vals.append(cv[1])
    return cols, vals

def insert(data):
    try:
        cols, vals = value_lists(data)
        query = f"INSERT INTO %s ({sput(cols)}) VALUES ({sput(vals)})"
        values = tuple(cols + vals)
        cur.execute(query, values)
        conn.commit()
    except:
        traceback.print_exception()

cur.close()
conn.close()

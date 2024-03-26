import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from -- nathanjh-28 -- in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect('postgres://flaskbballdb_user:D2QJhgX5jMUAZOw883TC9tgUY5ovJJK2@dpg-co1hgf7109ks73bsbtvg-a/flaskbballdb')
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def create():
    conn = psycopg2.connect('postgres://flaskbballdb_user:D2QJhgX5jMUAZOw883TC9tgUY5ovJJK2@dpg-co1hgf7109ks73bsbtvg-a/flaskbballdb')
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    """)
    conn.commit()
    
    conn.close()

    return "Basketball table was created with success!"

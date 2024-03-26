###############################################################################
#
#
# Title: 
# Flask + Render Deployment + Psycopg2 Lab for CSPB 3308 Spring '24
# 
# Author: 
# Nathan J Harris 
# 
# Usage: 
# go to the routes to see an example of creating a database creating a table, 
# inserting, selecting, and dropping the table.
# 
# github: 
# nathanjh-28
#
# CU ID:
# naha3153
# 
#
###############################################################################



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

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect('postgres://flaskbballdb_user:D2QJhgX5jMUAZOw883TC9tgUY5ovJJK2@dpg-co1hgf7109ks73bsbtvg-a/flaskbballdb')
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Basketball (First, Last, City, Name, Number) Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    """)
    conn.commit()
    conn.close()
    return "Basketball Table Populated with Success!"

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect('postgres://flaskbballdb_user:D2QJhgX5jMUAZOw883TC9tgUY5ovJJK2@dpg-co1hgf7109ks73bsbtvg-a/flaskbballdb')
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Basketball;
    """)
    records = cur.fetchall()
    conn.close()
    response_string = ""
    response_string += " <table> "
    for player in records:
        response_string+=' <tr> '
        for info in player:
            response_string += " <td> {} </td> ".format(info)
        response_string+=" </tr> "
    response_string += " </table> "
    return response_string

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect('postgres://flaskbballdb_user:D2QJhgX5jMUAZOw883TC9tgUY5ovJJK2@dpg-co1hgf7109ks73bsbtvg-a/flaskbballdb')
    cur = conn.cursor()
    cur.execute("""
        DROP TABLE Basketball;
    """)
    conn.commit()
    conn.close()
    return "Basketball Table was dropped with Success"
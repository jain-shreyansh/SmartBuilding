from flask import Flask,g
import sqlite3

app=Flask(__name__)

def connect_db():
    sql=sqlite3.connect('data.db')
    sql.row_factory=sqlite3.Row
    return sql

def get_db():
    if not hasattr(g,'sqlite3_db'):
        g.sqlite_db=connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()
 

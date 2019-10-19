import sqlite3 as sql
import os

def check_db():
    dbpath = os.path.join(os.path.dirname(__file__),'smarty.db')
    
    if not os.path.isfile(dbpath):
        conn = sql.connect(dbpath)
        conn.execute('''
        create table groceries (
            id integer primary key autoincrement,
            name text, 
            aptno integer,
            groc_list text,
            resolved integer
        );
         ''')
        conn.execute('''
        create table complaints (
            id integer primary key autoincrement,
            name text,
            aptno integer,
            complaint text,
            resolved integer
        );
         ''')

               
        


        conn.commit()
    else:
        conn = sql.connect(dbpath)

    conn.row_factory = sql.Row
    return conn


def insert_grocs(conn, aptno, name, grocs):
    conn.execute(f"""insert into groceries(name,aptno,groc_list,resolved)
     values ('{name}', {aptno},'{grocs}', 0)""")
    conn.commit()

def insert_complaint(conn, aptno, name, complaint):
    conn.execute(f"""insert into complaints(name,aptno,complaint,resolved)
     values ('{name}', {aptno},'{complaint}', 0)""")
    conn.commit()


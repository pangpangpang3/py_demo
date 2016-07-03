import sqlite3, os

def select_distinct():
    connect = sqlite3.connect('sqlite3_demo.db')
    cur = connect.cursor()
    cur.execute('select * from user where name == \'Green\'')
    values = cur.fetchall()
    print values
    print '\n'
    cur.execute('select distinct name from user')
    values = cur.fetchall()
    print("name column:", values)
    cur.close()
    connect.close()

def select_where():
    con = sqlite3.connect('sqlite3_demo.db')
    cur = con.cursor()
    cur.execute('select * from user where id == 10 and name == \'Peter\'')
    values = cur.fetchall()
    print values

    cur.execute('select * from user where name == \'Green\' or name == \'Peter\'')
    values = cur.fetchall()
    print values
    cur.close()

    con.close()

def query_order():
    con = sqlite3.connect('sqlite3_demo.db')
    cur = con.cursor()
    cur.execute('select name from user order by name')
    values = cur.fetchall()
    print("query by orders:\n")
    print values

if __name__ == '__main__':
    select_distinct()
    print('SELECT WHERE')
    select_where()
    query_order()


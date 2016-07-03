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

if __name__ == '__main__':
    select_distinct()

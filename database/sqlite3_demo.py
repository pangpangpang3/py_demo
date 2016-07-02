import sqlite3
import os

def create_database():
    if os.path.isfile('sqlite3_demo.db'):
        print("database is exist!")

    connect = sqlite3.connect('sqlite3_demo.db')
    curs = connect.cursor()

    curs = connect.execute('create table user(id int primary key, name varchar(20))')
    curs.execute('insert into user values(1, \'Tom\')')
    curs.execute('insert into user values(2, \'Emma\')')
    curs.execute('insert into user values(3, \'Allen\')')
    curs.execute('insert into user values(4, \'Tim\')')

    curs.close()
    connect.commit()
    connect.close()

def query_info(id_number):
    connect = sqlite3.connect('sqlite3_demo.db')
    cur = connect.cursor()

    cur = connect.execute('select * from user where id = %s' % id_number)
    values = cur.fetchall()
    print values
    cur.close()
    connect.close()

if __name__  == "__main__":
    create_database()
    info_list = query_info(2)

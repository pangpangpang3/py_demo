import sqlite3, os

def insert_info():
    connect = sqlite3.connect('sqlite3_demo.db')
    curs = connect.cursor()

    curs.execute('insert into user values(7, \'Timily\')')
    curs.execute('insert into user values(8, \'Ximily\')')
    curs.execute('insert into user values(9, \'Yimly\')')
    curs.execute('insert into user values(10, \'Peter\')')
    curs.execute('insert into user values(11, \'Purple\')')
    curs.execute('insert into user values(12, \'Green\')')
    curs.close()
    connect.commit()
    connect.close()

def select_name():
    connect = sqlite3.connect('sqlite3_demo.db')
    curs = connect.cursor()

    curs.execute('select name from user')
    values = curs.fetchall()
    print values
    curs.close()
    connect.commit()
    connect.close()

def select_id():
    connect = sqlite3.connect('sqlite3_demo.db')
    curs = connect.cursor()
    print "select all the id:\n"
    curs.execute('select id from user')
    values = curs.fetchall()
    print values
    curs.close()
    connect.commit()
    connect.close()

def select_id_range():
    connect = sqlite3.connect('sqlite3_demo.db')
    cur = connect.cursor()
    print "id range:\n"
    cur.execute('select * from user where id >= 2 and id < 4')
    values = cur.fetchall()
    print values
    cur.close()
    connect.commit()
    connect.close()

if __name__ == '__main__':
    insert_info()
    select_id()
    select_id_range()

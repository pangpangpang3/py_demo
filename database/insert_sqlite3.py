import sqlite3

def insert_into():
    con = sqlite3.connect('sqlite3_demo.db')
    cur = con.cursor()
    cur.execute('insert into user values(14, \'XiaMi\')')
    cur.execute('insert into user(id, name) values(15, \'Hui\')')
    cur.execute('insert into user(id, name) values(16, \'Xui\')')
    cur.execute('insert into user(id, name) values(17, \'Bob\')')
    cur.close()
    con.commit()
    con.close()

if __name__ == '__main__':
    insert_into()


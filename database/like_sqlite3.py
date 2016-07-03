import sqlite3

def like():
    con = sqlite3.connect('sqlite3_demo.db')
    cur = con.cursor()
    cur.execute('select * from user where name like \'T%\'')
    values = cur.fetchall()
    print values
    cur.close()
    con.close()


if __name__ == '__main__':
    like()


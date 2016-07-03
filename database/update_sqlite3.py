import sqlite3

def update_info():
    con = sqlite3.connect('sqlite3_demo.db')
    cur = con.cursor()
    cur.execute('update user set id = 20 where name == \'Bob\'')
    cur.execute('update user set id = 17 where name == \'Emma\'')
    cur.close()
    con.commit()
    con.close()


if __name__ == '__main__':
    update_info()

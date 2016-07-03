import sqlite3

def delete():
    con = sqlite3.connect('sqlite3_demo.db')
    cur = con.cursor()
    cur.execute('delete from user where id == 17')
    cur.execute('delete from user where id == 20')

    cur.close()
    con.commit()
    con.close()


if __name__ == '__main__':
    delete()

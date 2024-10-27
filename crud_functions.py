import sqlite3


def initiate_db():
    with sqlite3.connect('initiate.db') as db:
        cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Products(
     id integer PRIMARY KEY,
     title text NOT NULL,
     description text ,
     price integer NOT NULL);
     """)

    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price)VALUES(?,?,?)',
                       (f'Продукт{i}', f'описание{i}', i * 100))

    db.commit()


def get_all_products():
    with sqlite3.connect('initiate.db') as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM Products")

    db.commit()

    return cursor.fetchall()

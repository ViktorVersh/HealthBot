# import random
import sqlite3


def initiate_db():
    """
    Создаёт базу данных если её ещё нет
    """
    connection1 = sqlite3.connect("Products.db")
    cursor1 = connection1.cursor()

    cursor1.execute("""
    CREATE TABLE IF NOT EXISTS Products
        (id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL);
    """)

    cursor1.execute("""
    CREATE TABLE IF NOT EXISTS Users
        (id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL);
    """)

    connection1.commit()
    cursor1.close()


def get_all_products():
    """
    Получаем список всех товаров из таблицы
    :return: список товаров
    """
    connection2 = sqlite3.connect("Products.db")
    cursor2 = connection2.cursor()
    cursor2.execute("SELECT title, description, price FROM Products")
    products = cursor2.fetchall()
    product = []
    for i in products:
        product.append(f'Название товара: {i[0]}, Описание: {i[1]}, Цена: {i[2]}')
    cursor2.close()
    return product


def add_users(username, email, age):
    """
    Добавляем пользователя в таблицу
    :param username:
    :param email:
    :param age:
    :return: строка с именем добавленного пользователя
    """
    connection3 = sqlite3.connect("Products.db")
    cursor3 = connection3.cursor()
    cursor3.execute(f"INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)",
                    (username, email, age, 1000))
    connection3.commit()
    return f'Регистрация пользователя {username} прошла успешно'


def is_included(username):
    """
    Проверяем пользователя по базе данных
    :param username:
    :return: True если пользователь есть в таблице иначе False
    """
    connection4 = sqlite3.connect("Products.db")
    cursor4 = connection4.cursor()
    cursor4.execute("SELECT username FROM Users")
    users = cursor4.fetchall()
    for i in users:
        if i[0] == username:
            cursor4.close()
            return True
    cursor4.close()
    return False


if __name__ == '__main__':
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    initiate_db()
    for i in get_all_products():
        print(i)

    # print(get_all_products())
    print(is_included('User 30'))
    connection.commit()
    connection.close()

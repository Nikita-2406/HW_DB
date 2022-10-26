import psycopg2
def add_table(conn, cur):
    cur.execute("""
            CREATE TABLE IF NOT EXISTS names(
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(40),
            surname VARCHAR(40)
        );
    """)
    cur.execute("""
            CREATE TABLE IF NOT EXISTS email(
            email_id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES names(user_id),
            email VARCHAR(40)
        );
    """)
    cur.execute("""
            CREATE TABLE IF NOT EXISTS phone(
            phone_id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES names(user_id),
            number VARCHAR(13)
        );
    """)
    conn.commit()

def add_user(conn, cur):
    name, surname = input('Введите имя и фамилию:  ').split(' ')
    cur.execute("""INSERT INTO names(name, surname)
            values
            (%s, %s)
            RETURNING user_id;
    """, (name, surname))
    user_id = cur.fetchone()
    user_id = int(user_id[0])
    number = int(input('Введите номер телефона: '))
    cur.execute("""INSERT INTO phone(user_id, number)
            values
            (%s, %s) ;
    """, (user_id, number))
    email = input('Введите email: ')
    cur.execute("""INSERT INTO email(user_id, email)
            values
            (%s, %s);
    """, (user_id, email))
    conn.commit()

def add_phone_for_user(conn, cur):
    user_id = int(input('Введите id пользователя: '))
    number = input('Введите номер: ')
    cur.execute("""INSERT INTO phone(user_id, number)
            values
            (%s, %s);
    """, (user_id, number))
    conn.commit()

def update_names(conn, cur):
    user_id = int(input('Введите id пользователя: '))
    name, surname = input('Введите имя и фамилию: ').split(' ')
    cur.execute("""UPDATE names
            SET name = %s, surname = %s
            WHERE user_id = '%s';
    """, (name, surname, user_id))
    conn.commit()

def del_phone(conn, cur):
    number = input('Введите номер пользователя: ')
    cur.execute("""DELETE FROM phone
    WHERE number = %s;
    """, (number, ))
    conn.commit()

def delete_user(conn, cur):
    user_id = int(input('Введите id пользователя: '))
    cur.execute("""DELETE FROM email
    WHERE user_id = %s
    """, (user_id,))

    cur.execute("""DELETE FROM phone
    WHERE user_id = %s
    """, (user_id, ))

    cur.execute("""DELETE FROM names
    where user_id = %s
    """, (user_id, ))
    conn.commit()
def select_user(conn, cur):
    print('Выберите способ поиска: ')
    print('1)Имя')
    print('2)Фамилия')
    print('3)Номер телефона')
    print('4)email')
    com = int(input())
    meaning = input('Введите данные: ')
    if com == 1 :
        cur.execute("""SELECT n.user_id, name, surname, number, email FROM names n
                    JOIN phone p ON n.user_id = p.user_id
                    JOIN email e ON n.user_id = e.user_id
                    WHERE name = %s
            """, (meaning,))
    elif com == 2:
        cur.execute("""SELECT n.user_id, name, surname, number, email FROM names n
                    JOIN phone p ON n.user_id = p.user_id
                    JOIN email e ON n.user_id = e.user_id
                    WHERE surname = %s
            """, (meaning,))
    elif com == 3:
        cur.execute("""SELECT n.user_id, name, surname, number, email FROM names n
                    JOIN phone p ON n.user_id = p.user_id
                    JOIN email e ON n.user_id = e.user_id
                    WHERE number = %s
            """, (meaning,))
    else:
        cur.execute("""SELECT n.user_id, name, surname, number, email FROM names n
                    JOIN phone p ON n.user_id = p.user_id
                    JOIN email e ON n.user_id = e.user_id
                    WHERE email = %s
            """, (meaning,))
    fetch = cur.fetchone()
    if fetch == None:
        print('Пользователь не найден')
    else:
        print(fetch)
        user_id, name, surname, number, email = fetch
        print(f'ID - {user_id}')
        print(f'Имя - {name}')
        print(f'Фамилия - {surname}')
        print(f'Номер телефона - {number}')
        print(f'email - {email}')

def print_commands():
    print('at - Функция, создающая структуру БД (таблицы)')
    print('au - Функция, позволяющая добавить нового клиента')
    print('ap - Функция, позволяющая добавить телефон для существующего клиента')
    print('un - Функция, позволяющая изменить данные о клиенте')
    print('dp - Функция, позволяющая удалить телефон для существующего клиента')
    print('du - Функция, позволяющая удалить существующего клиента')
    print('su - Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)')
    print('stop - Остановить программу')

def commands():
    conn = psycopg2.connect(database="python_db", user="postgres", password="1")
    with conn.cursor() as cur:
        print_commands()
        while True:
            command = input('Введите команду: ')
            if command == 'at':
                add_table(conn, cur)
            if command == 'au':
                add_user(conn, cur)
            if command == 'ap':
                add_phone_for_user(conn, cur)
            if command == 'un':
                update_names(conn, cur)
            if command == 'dp':
                del_phone(conn, cur)
            if command == 'du':
                delete_user(conn, cur)
            if command == 'su':
                select_user(conn, cur)
            if command == 'stop':
                break
    conn.close()


if __name__ == '__main__':
    commands()
# Импорты
import sqlite3
from sqlite3 import Error
import datetime
import random

ID = 0
final = False
tovar_order = True
singin = True
brek = False
order_final = False
dostup = False
sty = ""
final_price = 0
final_count = 0
order_list = list()


#Подключение
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Подключение к БД произошло УСПЕШНО!")
    except Error as e:
        print(f"ERROR! '{e}' Что-то не так!")

    return connection
connection = create_connection("F:\Python\p50-7-20-Simonov-Egor-master\study-9\\RamenBD.sqlite")

def execute_query(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Запрос УСПЕШНЫЙ!") 
    except Error as e:
        print(f"ERROR! '{e}' Что-то не так!")


def select_table(query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"ERROR! '{e}' Что-то не так!")


def authorization(login, password):
    global ID, dostup, singin, sty, brek
    for user in users:
        if(user[4] == login and user[5] == password):
            print("\n ================================================ \n Добро пожаловать, Дорогой клиент! \n ================================================ \n")
            singin = False
            dostup = True
            ID = user[0]
            brek = True
            sty = "user"
            break
        else:
            sty = ""
            singin = True
            dostup = False
            ID = 0
    if(brek == False):
        for admin in admins:
            if(admin[6] == login and admin[7] == password):
                print("\n ================================================ \n Добро пожаловать, Серый кардинал! \n ================================================ \n")
                dostup = True
                singin = False
                ID = admin[0]
                sty = "admin"
                break
            else:
                sty = ""
                singin = True
                dostup = False
                ID = 0

    

def order():
    global final_price, final_count, order_final
    print("\n ============================= \n Выберите действие \n ============================= \n ")
    print("~ 1 -- Готовые блюда -- ")
    print("~ 2 -- Собрать рамен -- ")
    print("~ 3 -- Акции и Распродажи -- ")
    print("~ 4  -- Отменить текущий заказ -- ")
    print("")
    b = int(input("= "))
    if(b == 1):
        i = 0
        for product in products:
            if(i == 0):
                print(f"Название рамена: {product[1]}")
                print(f"Цена рамена: {product[3]}")
                print("Состав рамена:")
                price = product[3]
            print(f"{product[5]}")
            i = i + 1
        while order_final == False:
            print("")
            count = int(input("Выберите кол-во: "))
            print("")
            all_count = 0
            count_sources = 0
            for source in sources:
                count_sources += 1
                all_count += source[2]
            if(count * count_sources > all_count):
                print("Невозможно заказать! На складе недостаточно сырья!")
            else:
                order_final = True
        order_final = False
        final_count += count
        final_price += price * count
        print(f"Цена вашего заказа: {final_price}")
        oplata = int(input("Перейти к оплате? \n===========\n 1 - ДА \n 2 - НЕТ "))
        print("")
        if(oplata == 1):
            print(f"С вас {final_price} иена.")
            сoplata = int(input("Оплатить ? \n===========\n 1 - ДА \n 2 - НЕТ "))
            print("")
            if(сoplata == 1):
                for user in users:
                    if(ID == user[0]):
                        if(user[6] >= final_price):
                            execute_query(f"UPDATE users SET score_users = {user[6] - final_price} WHERE id_users = {user[0]};")
                        else:
                            print("На вашем счету нет или недостаточно средств! Приходите с достаточной суммой")
                            final_price = 0
                            final_count = 0
                            menu()
                soctav = ""
                for product in products:
                    soctav += f":{product[5]}:"
                oplatil(product[1], soctav)
            if(сoplata == 2):
                menu()
        if(oplata == 2):
            menu()
    elif(b == 2):
        soctav = ""
        for product in products:
            print(f"Навание: {product[1]}")
            break
        for source in sources:
            print(f"Хотите добавить {source[1]}?")
            op = int(input("\n===========\n 1 - Да \n 2 - Нет "))
            if(op == 1):
                soctav += f":{source[1]}:"
                while order_final == False:
                    print("Введите: сколько хотите дабавить")
                    opa = int(input("= "))
                    if(opa > source[2]):
                        print("Невозможно столько добавить!")
                    else:
                        final_price += source[3] * opa
                        order_final = True
                order_final = False
            elif(op == 2):
                print("")
            else:
                print("ERROR! Такого числа нет!")
        print("Введите количество таких блюд")
        opach = int(input("= "))
        print(f"Цена вашего заказа: {final_price}")
        oplata = int(input("Перейти к оплате ? \n 1 - ДА \n 2 - НЕТ "))
        if(oplata == 1):
            print(f"С вас {final_price} иена.")
            сoplata = int(input("Оплатить ? \n 1 - ДА \n 2 - НЕТ "))
            print("")
            if(сoplata == 1):
                for user in users:
                    if(ID == user[0]):
                        if(user[6] >= final_price):
                            execute_query(f"UPDATE users SET score_users = {user[6] - final_price} WHERE id_users = {user[0]};")
                        else:
                            print("На вашем счету нет или недостаточно средств! Приходите с достаточной суммой")
                            final_price = 0
                            final_count = 0
                            menu()
                oplatil(product[1], soctav)
            if(сoplata == 2):
                menu()
        if(oplata == 2):
            menu()
    elif(b == 3):
        b
    elif(b == 4):
        final_price = 0
        final_count = 0
    else:
        print("ERROR! Такого числа нет!")

def oplatil(productis, soctavs):
    global final_price, final_count
    for admin in admins:
            if(1 == admin[0]):
                execute_query(f"UPDATE admins SET score_admins = {admin[8] + final_price} WHERE id_admin = {admin[0]};")
    for user in users:
        if(ID == user[0]):
            if not user[7]:
                break
            else:
                final_price -= final_price / 100 * user[11]
                print(f"Ваша скидка {user[11]}")
                print("")
                break
    rand_subaru = random.randint(0, 2)
    rand_users = random.randint(0, 4)
    if(rand_subaru == 2):
        print("Вы нашли в рамене SUBARU! ")
        if(rand_users == rand_subaru):
            print("Вы уехали в закат!")
            soctavs += ", SUBARU"
            final_price -= final_price / 100 * 30
        else:
            print("Ничего необычного!")
            
    order_list.append(f"Название: {productis} | Состав: {soctavs} | Кол-во: {final_count}")
    print("Ваш чек:")
    print(datetime.datetime.now())
    print(f"{order_list[-1]} | Цена: {final_price}")
    print("")
    execute_query(f"INSERT INTO history (datatime_history, item_history, price_history, users_id) VALUES ('{datetime.datetime.now()}', '{order_list[-1]}', {final_price}, {ID});")
    for card in cards:
        if(final_price < 5000):
            break
        if(final_price < card[2]):
            execute_query(f"UPDATE users SET cards = {card[2] - 1} WHERE id_users = {ID};")
    final_price = 0
    final_count = 0

def menu():
    global final
    print("")
    print("\n ============================= \n Выберите действие \n ============================= \n ")
    print(" ~ 1 -- Посмотреть свой профиль -- ")
    print(" ~ 2 -- Сделать заказ -- ")
    print(" ~ 3 -- Выйти из раменной -- ")
    a = int(input(" = "))
    print("")
    if(a == 1):
        for user in users:
            if(user[0] == ID):
                print(f"ФИО: {user[1]} {user[2]} {user[3]}")
                print(f"Тайное имя: {user[4]} | Пароль: {user[5]}")
                print(f"Деньги: {user[6]}")
                print(f"Карта: {user[9]} | Скидка: {user[11]}")
                print("")
                print("~1 - Посмотреть историю покупок")
                tyu = int(input("= "))
                if(tyu == 1):
                    print(select_table(f"SELECT * FROM history WHERE users_id = {user[0]}"))
                else:
                    print("ERROR! Такого числа нет!")
                break
    elif(a == 2):
        order()
    elif(a == 3):
        final = True
    else:
        print("ERROR! Такого числа нет!")

def admin():
    global final, final_price, tovar_order
    for admin in admins:
        if(ID == admin[0]):
            print(f"Счет: {admin[8]}")
            break
    print("")
    print("\n ============================= \n Выберите действие \n ============================= \n ")
    print("~ 1 -- Посмотреть историю пользователя -- ")
    print("~ 2 -- Купить товары -- ")
    print("~ 3 -- Выйти -- ")
    a = int(input(" = "))
    print("")
    if(a == 1):
        num = int(input("Введите номер: "))
        for user in users:
            if(user[0] == num):
                print(select_table(f"SELECT * FROM history WHERE users_id = {user[0]}"))
                break
    elif(a == 2):
        while tovar_order == True:
            print(sources)
            print("")
            tovar = int(input("Выберите товар из списка: "))
            print("")
            for sour in sources:
                if(tovar == sour[0]):
                    tru = True
                    while tru == True:
                        cen = int(input("Укажите кол-во: "))
                        if(cen > sour[2]):
                            print("ERROR! Такого товара нет!")
                        else:
                            tru = False
                    execute_query(f"UPDATE sources SET count_sources = {sour[2] + cen} WHERE id_sources = {sour[0]};")
                    final_price += sour[3] * cen
                    print("Продолжить закупку?")
                    jo = int(input("\n 1 - Да \n 2 - Нет "))
                    if(jo == 1):
                        jo = 0
                        break
                    elif(jo == 2):
                        tovar_order = False
                    else:
                        print("ERROR! Такого числа нет!")
                else:
                    print("Такого товара нет!")
        tovar_order == True
        for admin in admins:
            if(ID == admin[0]):
                execute_query(f"UPDATE admins SET score_admins = {admin[8] - final_price} WHERE id_admin = {admin[0]};")
    elif(a == 3):
        final = True
    else:
        print("ERROR! Такого числа нет!")

users = select_table(f"SELECT * FROM users INNER JOIN cards ON cards.id_cards = users.cards_id")
admins = select_table("SELECT * FROM admins")
sources = select_table("SELECT * FROM sources")
products = select_table("SELECT * FROM products INNER JOIN sources ON sources.id_sources = products.sources_id")
cards = select_table(f"SELECT * FROM cards")

print("\n ========================================================================================== \n Добро пожаловать! Вы зашли в Akiba Ramen. Напишите тайное имя и пароль для входа \n ========================================================================================== \n")
while singin == True:
    log = input("\nТайное имя: ")
    pas = input("Пароль: ")
    authorization(log, pas)

if(dostup == True):
    while final == False:
        if(sty == "user"):
            menu()
        if(sty == "admin"):
            admin()

print(users)
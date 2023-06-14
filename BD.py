import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Подключение к БД произошло УСПЕШНО!")
    except Error as e:
        print(f"ERROR! '{e}' Что-то не так")

    return connection
connection = create_connection("F:\Python\p50-7-20-Simonov-Egor-master\study-9\\RamenBD.sqlite")

def execute_query(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Запросы - УСПЕШНО") 
    except Error as e:
        print(f"ERROR! '{e}' ЗАПРОСЫ шалят")

def create_db():
    try:
      execute_query(create_users_table)
      execute_query(create_users)

      execute_query(create_admins_table)
      execute_query(create_admins)

      execute_query(create_sources_table)
      execute_query(create_sources)

      execute_query(create_products_table)
      execute_query(create_products)

      execute_query(create_additions_table)

      execute_query(create_cards_table)
      execute_query(create_cards)

      execute_query(create_history_table)
      print("Создание БД произошло УСПЕШНО!") 
    except Error as e:
        print(f"ERROR!'{e}' Что-то не так")

create_cards_table = """
CREATE TABLE cards (
  id_cards INTEGER PRIMARY KEY AUTOINCREMENT,
  name_cards TEXT NOT NULL,
  price_cards DECIMAL(38,2) DEFAULT 0 NOT NULL,
  skidka_cards INTEGER NOT NULL
);"""
create_cards = """
INSERT INTO
  cards (name_cards, price_cards, skidka_cards)
VALUES
  ('Карта "Растущий интерес"', 5000, 5),
  ('Карта "Большой интерес"', 10000, 10),
  ('Карта "Особый интерес"', 15000, 15),
  ('Карта "Профессиональный интерес"', 20000, 20);
"""

create_users_table = """
CREATE TABLE users (
  id_users INTEGER PRIMARY KEY AUTOINCREMENT,
  secondname_users TEXT NOT NULL,
  firstname_users TETX NOT NULL,
  midllename_users TEXT,
  login_users TEXT NOT NULL,
  password_users TEXT NOT NULL,
  score_users DECIMAL(38,2) DEFAULT 0 NOT NULL,
  cards_id INTEGER,
  FOREIGN KEY (cards_id) REFERENCES cards(id_cards)
);"""
create_users = """
INSERT INTO
  users (secondname_users, firstname_users, midllename_users, login_users, password_users, cards_id, score_users)
VALUES
  ('User', 'User', 'User', 'User', 'User', 4, 550),
  ('User2', 'User2', 'User2', 'User2', 'User2', 4, 20000);
"""

create_admins_table = """
CREATE TABLE admins (
  id_admin INTEGER PRIMARY KEY AUTOINCREMENT,
  secondname_admin TEXT NOT NULL,
  firstname_admin TETX NOT NULL,
  midllename_admin TEXT,
  seriapass_admin INT NOT NULL,
  numberpass_admin INT NOT NULL,
  login_admin TEXT NOT NULL,
  password_admin NOT NULL,
  score_admins DECIMAL(38,2) DEFAULT 0 NOT NULL
);"""
create_admins = """
INSERT INTO
  admins (secondname_admin, firstname_admin, midllename_admin, seriapass_admin, numberpass_admin, login_admin, password_admin, score_admins)
VALUES
  ('Admin', 'Admin', 'Admin', 6655, 46247, 'Admin', 'Admin', 100000);
"""
create_sources_table = """
CREATE TABLE sources (
  id_sources INTEGER PRIMARY KEY AUTOINCREMENT,
  name_sources TEXT NOT NULL,
  count_sources INTEGER NOT NULL,
  price_sources DECIMAL(38,2) NOT NULL
);"""
create_sources = """
INSERT INTO
  sources (name_sources, count_sources, price_sources)
VALUES
  ('Лапша', 150, 15.6),
  ('Соба', 70, 14.6);
"""

create_products_table = """
CREATE TABLE products (
  id_products INTEGER PRIMARY KEY AUTOINCREMENT,
  name_products TEXT NOT NULL,
  sources_id INTEGER NOT NULL,
  price_products DECIMAL(38,2) NOT NULL,
  FOREIGN KEY (sources_id) REFERENCES sources(id_sources)
);"""
create_products = """
INSERT INTO
  products (name_products, sources_id, price_products)
VALUES
  ('Соя-рамэн', 1, 350);
"""

create_additions_table = """
CREATE TABLE additions (
  id_additions INTEGER PRIMARY KEY AUTOINCREMENT,
  name_additions TEXT NOT NULL,
  count_additions INTEGER NOT NULL,
  price_additions DECIMAL(38,2) NOT NULL
);"""
create_aditions = """
INSERT INTO
  additions (name_additions, count_additions, price_additions)
VALUES
  ('', 150, 15.6);
"""

create_history_table = """
CREATE TABLE history (
  id_history INTEGER PRIMARY KEY AUTOINCREMENT,
  datatime_history TEXT NOT NULL,
  item_history INTEGER NOT NULL,
  price_history DECIMAL(38,2) NOT NULL,
  users_id INETEGER NOT NULL,
  FOREIGN KEY (users_id) REFERENCES users(id_users)
);"""

create_db()
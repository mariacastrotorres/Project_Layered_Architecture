import requests
import os
from faker import Faker
import psycopg2

fake = Faker()

HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')
NAME = os.getenv('DB_NAME')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')

# HOST = "DB_A"
# PORT = "5432"
# NAME = "foo"
# USER = "postgres"
# PASSWORD = "bar123"


def connect_db():
    conn = psycopg2.connect(host=HOST, database=NAME, user=USER, password=PASSWORD)

    cur = conn.cursor()

    return cur

connect_db().execute("SELECT version()")


if __name__ == '__main__':
    print(connect_db().execute("SELECT version()"))
import requests
import os
from faker import Faker
import psycopg2
from random import randrange

fake = Faker()

HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')
NAME = os.getenv('DB_NAME')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')


def connect_db():
    conn = psycopg2.connect(host=HOST, database=NAME, user=USER, password=PASSWORD)
    return conn

def populate():
    sql = connect_db()
    cur = sql.cursor()
    for _ in range(100):
        r = requests.get('https://randomuser.me/api/')
        f = requests.get('https://randomfox.ca/floof/')

        if r.status_code == 200 and 'results' in r.json():
            nombre=r.json()['results'][0]['name']['first']
            apellido=r.json()['results'][0]['name']['last']
            imagen=r.json()['results'][0]['picture']['medium']
            cur.execute("INSERT INTO persona (nombre, apellido, imagen) VALUES (%s, %s, %s)",(nombre, apellido, imagen))
            sql.commit()
            cur.execute("SELECT id FROM persona ORDER BY id DESC LIMIT 1")
            print("Insertando persona")

            current = cur.fetchone()[0]
            for _ in range(randrange(1,3)):
                f = requests.get('https://randomfox.ca/floof/')
                if f.status_code == 200 and 'link' in f.json():
                    nombre=fake.unique.name()
                    imagen=f.json()['image']
                    cur.execute("INSERT INTO mascota (id_persona, nombre, imagen) VALUES (%s, %s, %s)",(current, nombre, imagen))
                    sql.commit()
                    print ("Insertando mascota")
    cur.close()
    sql.close()

            



if __name__ == '__main__':
    populate()

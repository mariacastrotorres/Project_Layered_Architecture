import os
import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


HOST = os.getenv('DB_HOST0')
PORT = os.getenv('DB_PORT')
NAME = os.getenv('DB_NAME')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')

CORS(app)


try:
    conn = psycopg2.connect(host=HOST, database=NAME, user=USER, password=PASSWORD)
    cur = conn.cursor()

    @app.route('/persona/<int:persona_id>')
    def fetch_by_id(persona_id=None):
        persona = []
        mascota = []
        cur.execute(f'SELECT id, nombre, imagen FROM mascota WHERE id_persona = {persona_id}')
        rows2 = cur.fetchall()

        for row in rows2:
            temp2 = dict(id_mascota = row[0], nombre = row[1], imagen = row[2])
            mascota.append(temp2)

        cur.execute(f'SELECT nombre, apellido, imagen FROM persona WHERE id = {persona_id}')
        rows = cur.fetchall()
        temp = dict(nombre = rows[0][0], apellido = rows[0][1], imagen = rows[0][2], mascotas = mascota)
        persona.append(temp)
        return jsonify(items = [persona])

    @app.route('/mascota/<int:mascota_id>')
    def obtener_mascota(mascota_id=None):
        persona = []
        mascota = []
        cur.execute(f'SELECT id_persona, nombre, imagen FROM mascota WHERE id = {mascota_id}')
        rows = cur.fetchall()
        persona_id = rows[0][0]
        cur.execute(f'SELECT nombre, apellido, imagen FROM persona WHERE id = {persona_id}')
        rows2 = cur.fetchall()
        temp2 = dict(nombre = rows2[0][0], apellido = rows2[0][1], imagen = rows2[0][2])
        temp = dict(nombre = rows[0][1], imagen = rows[0][2], dueno = persona)
        persona.append(temp2)
        mascota.append(temp)
        print(persona)
        return jsonify(items = [mascota])

    @app.route('/add-persona', methods=['GET', 'POST'])
    def add_persona():
        if request.method == 'POST':
            data = request.form.to_dict()
            print(data)
            cur.execute("INSERT INTO persona (nombre, apellido, imagen) VALUES (%s, %s, %s)",(f"{data['nombre']}", f"{data['apellido']}", data['imagen']))
            conn.commit()
            return 'Persona agregada'
        else:
            return 'Algo falló'

    @app.route('/add-mascota', methods=['GET', 'POST'])
    def add_mascota():
        if request.method == 'POST':
            data = request.form.to_dict()
            print(data)
            cur.execute("INSERT INTO mascota (id_persona, nombre, imagen) VALUES (%s, %s, %s)",(f"{data['id_persona']}", f"{data['nombre']}", data['imagen']))
            conn.commit()
            return 'Mascota agregada'
        else:
            return 'Algo falló'

    @app.route('/delete-mascota', methods=['GET', 'DELETE'])
    def delete_mascota_by_id():
        mascota_id = request.form.to_dict()
        print(mascota_id['mascotaId'])
        cur.execute(
            f"DELETE FROM mascota WHERE id = {mascota_id['mascotaId']} RETURNING nombre")
        conn.commit()

        return 'Mascota Eliminada'

    @app.route('/delete-persona', methods=['GET', 'DELETE'])
    def delete_mascota_by_id():
        persona_id = request.form.to_dict()
        print(persona_id['personaId'])
        cur.execute(
            f"DELETE FROM mascota WHERE id_persona = {persona_id['personaId']} RETURNING nombre")
        cur.execute(
            f"DELETE FROM persona WHERE id = {persona_id['personaId']} RETURNING nombre")
        conn.commit()

        return 'Persona Eliminada'






except:
    print('Error')


if __name__ == '__main__':
    app.run(host= "0.0.0.0", port=5000, debug=True)



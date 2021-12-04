import requests
from faker import Faker
from app.models import Mascota, Persona
from models import Mascota , Persona

fake = Faker()

for _ in range(50):
    r = requests.get('https://randomuser.me/api/')
    f = requests.get('https://randomfox.ca/floof/')
    
    if f.status_code == 200 and 'link' in f.json():
        mascota = Mascota(
            nombre=fake.unique.name(),
            imagen=f.json()['image']
        )
        print(f"##### Insertando registro...\n\t-> Registro: {mascota}\n\t-> Status: {mascota.save()}")
    if r.status_code == 200 and 'file' in r.json():
        persona = Persona(
            nombre=r.json()['results'][0]['name']['first'],
            apellido=r.json()['results'][0]['name']['last'],
            imagen=r.json()['results'][0]['picture']['medium']
        )
        print(f"##### Insertando registro...\n\t-> Registro: {persona}\n\t-> Status: {persona.save()}")
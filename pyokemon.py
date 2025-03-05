import requests

def obtener_datos_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        nombre = datos["name"]
        id_pokemon = datos["id"]
        altura = datos["height"]
        peso = datos["weight"]
        tipos = [tipo["type"]["name"] for tipo in datos["types"]]

        print(f"Nombre: {nombre.capitalize()}")
        print(f"ID: {id_pokemon}")
        print(f"Altura: {altura}")
        print(f"Peso: {peso}")
        print(f"Tipo(s): {', '.join(tipos)}")
    else:
        print("Pokémon no encontrado.")

# Solicitar el nombre del Pokémon al usuario
nombre_pokemon = input("Introduce el nombre de un Pokémon: ")
obtener_datos_pokemon(nombre_pokemon)

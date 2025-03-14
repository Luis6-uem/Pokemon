import requests
import tkinter as tk
from tkinter import Label, Entry, Button
from PIL import Image, ImageTk
from io import BytesIO

def obtener_datos_pokemon():
    nombre_pokemon = entrada.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        nombre = datos["name"].capitalize()
        id_pokemon = datos["id"]
        altura = datos["height"]
        peso = datos["weight"]
        tipos = ", ".join([tipo["type"]["name"].capitalize() for tipo in datos["types"]])
        url_imagen = datos["sprites"]["front_default"]


        etiqueta_resultado.config(text=f"Nombre: {nombre}\nID: {id_pokemon}\nAltura: {altura}\nPeso: {peso}\nTipo(s): {tipos}")

        imagen_respuesta = requests.get(url_imagen)
        imagen_bytes = Image.open(BytesIO(imagen_respuesta.content))
        imagen = ImageTk.PhotoImage(imagen_bytes)
        etiqueta_imagen.config(image=imagen)
        etiqueta_imagen.image = imagen
    else:
        etiqueta_resultado.config(text="Pokémon no encontrado.")
        etiqueta_imagen.config(image="")

ventana = tk.Tk()
ventana.title("Pokedex")
ventana.geometry("300x400")

Label(ventana, text="Introduce el nombre del Pokémon:").pack()
entrada = Entry(ventana)
entrada.pack()

Button(ventana, text="Buscar", command=obtener_datos_pokemon).pack()

etiqueta_resultado = Label(ventana, text="", justify="left")
etiqueta_resultado.pack()

etiqueta_imagen = Label(ventana)
etiqueta_imagen.pack()

ventana.mainloop()

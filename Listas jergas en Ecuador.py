meme_dict = {
            "MAN": "Hombre, chico, tipo",
            "SIMÓN": "Sí",
            "DE LEY": "Por supuesto, obligatoriamente",
            "CHIRO": "Estar sin dinero",
            "FARRA": "Fiesta",
            "CHORO": "Ladrón",
            "CAMELLAR": "Trabajar",
            "NARANJAS": "No, nada",
            "LOCO/A": "Amigo o persona cercana"
            }


word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")


if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Palabra no encontrada")

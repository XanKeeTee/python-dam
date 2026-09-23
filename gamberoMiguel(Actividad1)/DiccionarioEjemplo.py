def main():
    diccionario = [
        {"Nombre": "Miguel", "Apellido": "Gambero", "Edad": 19},
        {"Nombre": "Daniel", "Apellido": "Gambero", "Edad": [19, 12, 14]},
    ]
    ## print(diccionario[1]["Edad"][1])

    conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    conjunto.add(10)
    conjunto.remove(1)
    ## print(conjunto)


if __name__ == "__main__":
    main()
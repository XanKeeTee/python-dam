## 5.1. Crea la estructura de programa principal, donde incluirás todo el código solicitado en los siguientes pasos. 
def main():
    
    ## 5.2. Crea una lista con los siguientes elementos, en el mismo orden: Manzana, Pera, Melocotón.
    lista1 = ["Manzana", "Pera", "Melocoton"]
    
    ## 5.3. Crea o5tra lista con los siguientes elementos, en el mismo orden: Kiwi, Sandía, Melón. 
    lista2 = ["Kiwi","Sandia","Melon"]
    
    ##5.4. Añade la segunda lista a la primera.     
    lista1.extend(lista2)
    
    ##5.5. Muestra el último elemento de la lista. 
    print("El ultimo elemento de la lista es: ", lista1[-1])
    
    ## 5.6. Crea una tupla con los números 3, 5 y 7. 
    tupla = (3,5,7)
    
    ## 5.7. Muestra el primer elemento de la tupla. 
    print("El primer elemento de la tupla es: ", tupla[0])
    
    ##5.8. Crea un rango con los parámetros inicio, fin y salto determinados por tres campos input donde el usuario pueda introducir sus valores. 
    inicio = int(input("Digame el primer numero: "))
    fin = int(input("Digame el segundo numero: "))
    salto = int(input("Dame el salto entre sus valores: "))
    
    rango = range(inicio,fin,salto)
    
    ##5.9. Muestra el rango. 
    print(rango[2])
    
if __name__ == "__main__":
    main()
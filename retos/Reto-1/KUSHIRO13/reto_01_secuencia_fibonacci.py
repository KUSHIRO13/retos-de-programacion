"""
Reto 1: Secuencia de Fibonacci
Objetivo: Realizar una funcion que calcule la cantidad de iteracion proporcionada por el usuario
y que esta misma sea el límite de la cantidad de iteraciones de la funcion
"""


# Se crea la funcion del reto propuesto
def fibonacci(n):
    recursiva = []
    if n == 1 or n == 0:  # Se comprueba si el numero digita es igual a cero o uno
        recursiva.append(1)
        return recursiva
    else:
        """
        Si la condicion anterior es falsa se crea un bucle en donde el limite sera el valor digitado
        """
        for fn in range(0, n):
            # Esta condicion es importante para la suma porque obliga al programa agregar el valor de uno
            if len(recursiva) == 0 or len(recursiva) == 1:
                recursiva.append(1)
            else:
                # Se suma los dos ultimos valores y se agregan al largo de la lista
                recursiva.insert(len(recursiva), recursiva[-1] + recursiva[-2])
    return recursiva


print(" Bienvenido al Reto 1 ".center(32, "="))

recursivo = int(input("Favor de ingresar un numero: "))
res = fibonacci(recursivo)
for f in res:
    print(f)

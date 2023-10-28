import random
import time


random.seed(42)


def generar_numeros_aleatorios(minimo, maximo):
    return random.randint(minimo, maximo)


def operacion_numeros(operacion, tiempo_limite):
    print(f"Iniciando operación de {operacion} durante {tiempo_limite} segundos.")
    end_time = time.time() + tiempo_limite  
    while time.time() < end_time:
        numero1 = generar_numeros_aleatorios(1, 100)
        numero2 = generar_numeros_aleatorios(1, 100)

        if operacion == "resta":
            resultado = numero1 - numero2
        elif operacion == "suma":
            resultado = numero1 + numero2
        elif operacion == "multiplicacion":
            resultado = numero1 * numero2
        elif operacion == "division":
            if numero2 == 0:
                print("No se puede dividir por cero.")
                continue  
            resultado = numero1 / numero2
        else:
            print(f"Operación no válida: {operacion}")
            break  

        print(f"Números utilizados para {operacion}: {numero1} y {numero2}")
        print(f"Resultado de {operacion}: {resultado}")


min_tiempo = 5 
max_tiempo = 15  

operaciones = ["resta", "suma", "division", "multiplicacion"]


for operacion in operaciones:
    tiempo = random.uniform(min_tiempo, max_tiempo)
    operacion_numeros(operacion, tiempo)

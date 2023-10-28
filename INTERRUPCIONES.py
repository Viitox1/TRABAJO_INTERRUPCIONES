import random
import time


def generar_num_aleatorio(min_val, max_val):
    return random.randint(min_val, max_val)


def realizar_operacion(oper, tiempo_limite):
    start = time.time()
    print(f"Iniciando operación de {oper} durante {tiempo_limite} segundos.")
    while time.time() - start < tiempo_limite:
        num1 = generar_num_aleatorio(1, 100)
        num2 = generar_num_aleatorio(1, 100)
        resultado = None  

        if oper == "resta":
            resultado = num1 - num2
        elif oper == "suma":
            resultado = num1 + num2
        elif oper == "multiplicacion":
            resultado = num1 * num2
        elif oper == "division":
            resultado = num1 / num2

        print(f"Números utilizados para {oper}: {num1} y {num2}")
        
        if resultado is not None:
            print(f"Resultado de {oper}: {resultado}")


tiempo_minimo = 5  
tiempo_maximo = 15  


while True:
    realizar_operacion("resta", random.uniform(tiempo_minimo, tiempo_maximo))
    realizar_operacion("suma", random.uniform(tiempo_minimo, tiempo_maximo))
    realizar_operacion("division", random.uniform(tiempo_minimo, tiempo_maximo))
    realizar_operacion("multiplicacion", random.uniform(tiempo_minimo,tiempo_maximo))
number1 = int(input("ingresa un número:"))
number2 = int(input("ingresar otro número:"))

elección = 0

while elección != 6:
    print("""
    indique la operación a relalizar:

    1) Suma
    2) Resta
    3) Multiplicación 
    4) División
    5) Cambio de valores
    6) Salir
    """)

    elección = int(input())

    if elección == 1:
        print(" ")
        print("Resultado: ", number1, "+", number2, "=", number1+number2)

    if elección == 2:
        print(" ")
        print("Resultado: ", number1, "-", number2, "=", number1-number2)

    if elección == 3:
        print(" ")
        print("Resultado: ", number1, "*", number2, "=", number1*number2)

    if elección == 4:
        print(" ")
        print("Resultado: ", number1, "/", number2, "=", number1/number2)

    if elección == 5:
        number1 = int(input("ingresa un número:"))
        number2 = int(input("ingresar otro número:"))

    if elección == 6:
        print("Gracias por usar la calculadora, Creada por Julio Sanchez")

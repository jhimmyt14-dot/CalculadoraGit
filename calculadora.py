def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicacion(a, b): return a * b
def division(a, b):
    if b == 0: return "Error: División por cero"
    return a / b
def potencia(a, b): return a ** b

historial = [] # Aquí guardaremos las operaciones

while True:
    print("\n--- MENÚ CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Ver Historial")
    print("7. Salir")
    
    opcion = input("Elige una opción (1-7): ")

    if opcion == '7':
        print("¡Calculadora terminada!")
        break
    
    if opcion == '6':
        print("\n--- HISTORIAL DE OPERACIONES ---")
        if len(historial) == 0:
            print("No hay operaciones aún.")
        else:
            for op in historial:
                print(op)
        continue

    if opcion in ['1', '2', '3', '4', '5']:
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Por favor ingresa solo números.")
            continue

        if opcion == '1':
            resultado = suma(num1, num2)
            texto_op = f"{num1} + {num2} = {resultado}"
        elif opcion == '2':
            resultado = resta(num1, num2)
            texto_op = f"{num1} - {num2} = {resultado}"
        elif opcion == '3':
            resultado = multiplicacion(num1, num2)
            texto_op = f"{num1} * {num2} = {resultado}"
        elif opcion == '4':
            resultado = division(num1, num2)
            texto_op = f"{num1} / {num2} = {resultado}"
        elif opcion == '5':
            resultado = potencia(num1, num2)
            texto_op = f"{num1} ** {num2} = {resultado}"

        print(f"\nResultado: {resultado}")
        historial.append(texto_op) # Agregamos al historial
    else:
        print("Opción no válida. Intenta de nuevo.")
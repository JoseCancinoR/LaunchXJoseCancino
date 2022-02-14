from datetime import date

# program.py
sum = 1 + 2
print(sum)

sum = 1 + 2  # 3
product = sum * 2
print(product)

# Tipos de datos
planetas_en_el_sistema_solar = 8
distancia_a_alfa_centauri = 4.367  # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11"  # string

left_side = 10
right_side = 5
left_side / right_side  # 2

# Fecha
date.today()
print(date.today())

# Fecha con concatenacion
print("Today's date is: " + str(date.today()))

# Entrada de dato (Usuario)
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

# Calculadora
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))

print("***********")
print("** CALCU **")
print("** LATOR **")
print("**by lani**")
print("***********")

print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")
print("5.Potencia")
print("Raíz-cuadrada")
print("7.Raíz n-ésima")

opcion = input("Elige una opción (1-7:)")

# Para operaciones de 2 numeros:
if opcion in ["1","2","3","4","5","7"]:
    num1 = float(input("Primer numero:"))
    num2 = float(input("Segundo numero"))

# Para raíz cuadrada (solo un numero):
elif opcion == "6":
    num1 = float(input("Numero:"))

#Operaciones:
if opcion == "1":
    resultado = num1 + num2

elif opcion == "2":
    resultado = num1 - num2

elif opcion == "3":
    resultado == num1 * num2

elif opcion == "4":
    if num2 != 0:
     resultado = num1 / num2
    else:
     resultado = "Error: No se puede dividir entre 0!"

elif opcion == "5":
    resultado = num1 ** num2 #potencia

elif opcion == "6":
    if num1 >= 0:
     resultado = math.sqrt(num1)
    else:
     resultado = "Error: No se puede sacar raíz cuadrada de 0!"

elif opcion == "7":
    #raíz n´ésima = num1 ** (1/num2)
    if num2 !=0:
        resultado = num ** (1 / num2)
    else:
        resultado = "Error: raiz n-ésima no puede tener n=0"
else:
    resultado = "Opcion no válida"

print("Resultado:", resultado)
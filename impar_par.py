num1 = int(input("Inserta un número: "))
num2 = int(input("Pon otro número: "))

if num1%2==0 and num2%2==0:
    print("Todos son pares.")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} es par. {num2} es impar")
elif num1%2!=0 and num2%2==0:
    print(f"{num1} es impar. {num2} es par.")    
else:
    print("Todos son impares.")            
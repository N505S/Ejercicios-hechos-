num1 = int(input("Inserte un número: "))
num2 = int(input("Añada otro número: "))

op = input(f"Sume poniendo 's', restar 'r', multiplique con 'm' y dividir 'd': ").lower()

s = num1+ num2
r = num1 - num2
m = num1 * num2
d = num1 / num2

if  op == 's':
    print(f"{s}")

elif op == 'r':
    print(f"{r}")

elif op == 'm':
    print(f"{m}")

elif op == 'd':
    print(f"{d}")

else:
    print(f"pipopipo errorcillo")





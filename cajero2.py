saldo = 1000

print("\t.:MENU:.")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero en la cuenta")
print("4. Salir")
opcion = int(input("Digite una opción de menu: "))

print()

if opcion==1:
    extra = float(input("Cuánto dinero quiere ingresar -> "))
    saldo += extra
    print(f"Dinero disponible: {saldo}€")
elif opcion==2:
    retirar = float(input("Cuánto dinero quiere retirar -> "))
    if retirar>saldo:
        print("No podees!")
    else:
        saldo -= retirar
        print(f"Dinero disponible: {saldo}€")
elif opcion == 3:
    print(f"Tiene -> {saldo}€")
elif opcion == 4:
    print("Enga hasta luego")
else:
    print("Señore me pones 1, 2, 3, 4. Que si no vamos mal.")
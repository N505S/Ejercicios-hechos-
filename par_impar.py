def main():
    numero_1 = int(input("Escriba un número entero: "))
    ##numero_3 = 0
    numero_2 = int(input(f"Escriba un número entero mayor o igual que {numero_1}:"))

    if numero_2 < numero_1:
        print(f"!QUE ESCRIVAS UN NÚMERO ENTERO MAYOR O IGUAL QUE {numero_1}!")
    else:
        for i in range (numero_1, numero_2+1):
            if i % 2 == 0:
                print(f"El número {i} es par.")
            else:
                print(f"El número {i} es impar.")
if __name__ == "__main__":
    main()



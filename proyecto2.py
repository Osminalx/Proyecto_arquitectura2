# Está función convierte los números de decimal a binario, es la base de todo el programa
def toBinary(nume: int):
    residuos = []
    if nume < 0:
        num = nume * -1
        while num != 0:
            residuos.insert(0, num % 2)
            num //= 2
        if (len(residuos) >= 17):
            print(residuos, " Overflow")
            return residuos
        else:
            for i in range(0, 16):
                if len(residuos) < 16:
                    residuos.insert(0, 0)
            print(residuos)
            print(len(residuos))
            return C2(Negate(residuos))
    else:
        num = nume
        while num != 0:
            residuos.insert(0, num % 2)
            num //= 2
        if (len(residuos) >= 17):
            print(residuos, " Overflow")
            return residuos
        else:
            for i in range(0, 16):
                if len(residuos) < 16:
                    residuos.insert(0, 0)
            print(residuos)
            print(len(residuos))
            return residuos

# Esta función toma como argumento una lista de numeros enteros(formato de los números binarios de este programa)
# y los convierte a complemento a 1


def Negate(residuos: list[int]):
    suodiser = []
    for i in range(len(residuos)):
        if residuos[i] == 0:
            suodiser.insert(i, 1)
        else:  # ver si funciona con tan solo else
            suodiser.insert(i, 0)
    print("C1 = ", suodiser)
    print(len(suodiser))
    return suodiser

# Esta función toma una lista de enteros(formato de los binarios) y le añade un 1, para hacerlo
# complemento a 2


def C2(suodiser: list[int]):
    complemento2 = []
    for i in range(len(suodiser)-1, 0, -1):
        if suodiser[i] == 0:
            suodiser.pop(i)
            suodiser.insert(i, 1)
            break
        elif suodiser[i] == 1:
            suodiser.pop(i)
            suodiser.insert(i, 0)
    print("C2 = ", suodiser)
    return suodiser


# Un intento distinto del complemnto a dos, que se quedó comentado
""" def C2(suodiser: list[int]):
    complemento2 = []
    for i in range(len(suodiser)-1, 0, -1):
        if suodiser[i] == 0:
            complemento2.insert(i, 1)
            break
        elif suodiser[i] == 1:
            complemento2.insert(i, 0)
            
    return complemento2 """

# suma de binarios


def sum(num: int, num2: int):
    bin1 = toBinary(num)
    bin2 = toBinary(num2)
    sumdec = num+num2
    sumbin = toBinary(sumdec)
    print(sumdec)

# resta de binarios


def resta(num1: int, num2: int):
    bin1 = toBinary(num1)
    bin2 = toBinary(num2)
    restaDec = num1 - num2
    if restaDec < 0:
        pos = restaDec * -1
        result = C2(Negate(toBinary(pos)))
        print("La resta decimal es: ", restaDec)
        return result
    else:
        print("La resta decimal es: ", restaDec)
        resta = toBinary(restaDec)
        return resta

# Esta función compara que número es mayor o si son iguales


def comp(num1: int, num2: int):
    bin1 = toBinary(num1)
    bin2 = toBinary(num2)
    if num1 < 0:
        nume1 = num1*-1
        bin1 = C2(Negate(toBinary(nume1)))
    elif num2 < 0:
        nume2 = num2*-1
        bin2 = C2(Negate(toBinary(nume2)))

    if num1 < num2:
        print(bin1, " < ", bin2)
    elif num1 > num2:
        print(bin1, " > ", bin2)
    elif num1 == num2:
        print(bin1, " = ", bin2)

# comentarios para copy paste
# entrada1 = input("ingresa un número entero sin signo: ")
# entrada2 = input("ingresa un número entero sin signo: ")
# num1 = int(entrada1)
# num2 = int(entrada2)


# Menú
salir = True

while salir == True:
    print("opciones: ")
    print("1.- Conversión a binario")
    print("2.- Suma binaria")
    print("3.- Negación binaria C1")
    print("4.- Negación binaria C2")
    print("5.- Resta binaria")
    print("6.- Comparación")
    print("7.- Salir")
    opt = input("ingresa una opción: ")
    option = int(opt)

    if option == 1:
        entrada1 = input("ingresa un número entero sin signo: ")
        num1 = int(entrada1)
        # if num1 < 0:
        #     C2(Negate(toBinary(Neg(num1))))
        # else:
        toBinary(num1)
    elif option == 2:
        entrada1 = input("ingresa un número entero sin signo: ")
        entrada2 = input("ingresa un número entero sin signo: ")
        num1 = int(entrada1)
        num2 = int(entrada2)
        if num1 < 0:
            resta(num2, num1)
        elif num2 < 0:
            resta(num1, num2)
        sum(num1, num2)
    elif option == 3:
        entrada1 = input("ingresa un número entero sin signo: ")
        num1 = int(entrada1)
        Negate(toBinary(num1))
    elif option == 4:
        entrada1 = input("ingresa un número entero sin signo: ")
        num1 = int(entrada1)
        C2(Negate(toBinary(num1)))
    elif option == 5:
        entrada1 = input("ingresa un número entero sin signo: ")
        entrada2 = input("ingresa un número entero sin signo: ")
        num1 = int(entrada1)
        num2 = int(entrada2)
        resta(num1, num2)
    elif option == 6:
        entrada1 = input("ingresa un número entero sin signo: ")
        entrada2 = input("ingresa un número entero sin signo: ")
        num1 = int(entrada1)
        num2 = int(entrada2)
        comp(num1, num2)
    elif option == 7:
        salir = False
    else:
        print("Opción no válida ")

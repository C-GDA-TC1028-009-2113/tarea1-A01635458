def main():
    #escribe tu código abajo de esta línea
    inicial =int(input("Dame el peso inicial: "))
    final =int(input("Dame el peso final: "))
    meses =int(input("Dame la cantidad de meses: "))

    bajar =(inicial-final)/meses
    print("Lo que debes bajar por mes es:",bajar)

    pass



if __name__ == '__main__':
    main()

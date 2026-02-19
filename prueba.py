numero = 0

while (numero != 5):
  numero = int(input("Ingresa una opcion: 1) Jugar 2) Opciones 3) Personajes 4) Musica 5) Salir : "))
  match(numero):
    case 1:
        print("....Jugando...")
    case 2:
        print("....Opciones...")
    case 3:
        print("....Personajes...")
    case 4:
        print("....Musica...")
    case 5:
        print("....Saliendo...")
    case _:
        print("...Opcion no valida...")
        print("adios")
        print("algo")
        break


print("Fuera del ciclo")
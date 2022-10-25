print("""
***************************************************
            ___  ___ _____  _   _  _   _
            |  \/  ||  ___|| \ | || | | |
            | .  . || |__  |  \| || | | |
            | |\/| ||  __| | . ` || | | |
            | |  | || |___ | |\  || |_| |
            \_|  |_/\____/ \_| \_/ \___/
***************************************************
**************SELECCIONE UNA OPCION:***************
***************************************************
""")
lista = []
while (True):
    print("""
**Agregar lista de informacion............(1)
**Mostrar listados ingresados ............(2)
**Salir de la aplicacion ............(3)
***************************************************""")
    opcion = int(input())
    if opcion == 1:
        print("procesando peticion...")
        while (True):
            dato =input("ingrese el dato que desea registrar ")
            lista.append(dato)
            print("desea agregar otro dato?")
            res = input()
            if(res == 'no'): break
    elif opcion == 2:
        print("mostrando datos...")
        print(lista)
    elif opcion == 3:
        print("Adios...")
        break
    else: print("ERROR: Comando desconocido")



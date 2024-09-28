import re

def main():
    print("Bienvenido!")
    #ruta = input("Ingrese la ruta del archivo a leer:\n")
    archivo_llegada =open("archivo_llegada.txt","r")
    archivo_respuesta=open("archivo_respuesta.txt","w")

    patrones = input('Ingrese el patron \n')

    patrones = re.sub(',','|',patrones)

    for linea in archivo_llegada.readlines():
        archivo_respuesta.write(re.sub(patrones, '', linea))

    archivo_llegada.close()
    archivo_respuesta.close()

if __name__ == '__main__':
    main()
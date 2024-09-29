import re

def main():

        ruta_llegada = input('Ingrese la ruta del archivo (ejemplo: archivo_leer)\n')
        archivo_llegada = open(f'{ruta_llegada}.txt', "r")

        ruta_respuesta = input('Ingrese el nombre del archivo donde se guardara (ejemplo: archivo_respuesta)\n')
        archivo_respuesta = open(f'{ruta_respuesta}.txt', "w")

        # Solicitamos el patrón al usuario
        patrones = input('Ingrese el patrón separado por comas (ejemplo: man,s,tu)\n')

        # Separamos el input en una lista de patrones
        lista_patrones = patrones.split(',')

        # Esta funcion genera nuestra expresion regular
        # {a..z+A..Z+1..0}*.(Patron).{a..z+A..Z+1..0} | {a..z+A..Z+1..0}*.(Patron).{a..z+A..Z+1..0}
        patron = '|'.join([fr'\w*{patron}\w*' for patron in lista_patrones])
        print(f'Patrón generado: {patron}')

        # Se reemplaza el patron por ''
        archivo_respuesta.write(re.sub(patron, '', archivo_llegada.read()))

        print("Su archivo se genero con exito en la carpeta del proyecto :)")

        # Se cierran los archivos
        archivo_llegada.close()
        archivo_respuesta.close()

if __name__ == '__main__':
    try:
        print("╔" + "═" * 13 + "╗")
        print("║ Bienvenido! ║")
        print("╚" + "═" * 13 + "╝")
        main()
    except:
        print("Ocurrio un error inesperado :(")

import re


def main():
    print("Bienvenido!")

    # Abrimos los archivos
    archivo_llegada = open("archivo_llegada.txt", "r")
    archivo_respuesta = open("archivo_respuesta.txt", "w")

    # Solicitamos el patrón al usuario
    patrones = input('Ingrese el patrón separado por comas (ejemplo: man,s,tu)\n')

    # Separamos el input en una lista de patrones
    lista_patrones = patrones.split(',')

    patron = '|'.join([fr'\b\w*{patron}\w*\b' for patron in lista_patrones])

    print(f'Patrón generado: {patron}')  # Esto imprime el patrón generado para verificar

    archivo_respuesta.write(re.sub(patron, '', archivo_llegada.read()))

    archivo_llegada.close()
    archivo_respuesta.close()

if __name__ == '__main__':
    main()

def main():
    try:
        configuration = open("config.txt")
    except FileNotFoundError:
        print("No se puede encontrar el archivo config.txt ")
    except IsADirectoryError:
        print("Se encontró config.txt pero este es un directorio, no puede leerse")
    except (BlockingIOError, TimeoutError):
        print('Sistema bajo sobrecarga, No se puede completar la lectura')

if __name__ == '__main__':
    main()


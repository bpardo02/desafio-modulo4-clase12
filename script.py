# script.py
import json
from usuario import Usuario


def main():
    usuarios = []  # Lista para almacenar las instancias de Usuario
    try:
        with open("usuarios.txt", "r") as file:
            for line in file:
                try:
                    # Intentar cargar la línea como JSON
                    data = json.loads(line.strip())

                    # Crear una instancia de Usuario con los datos del JSON
                    usuario = Usuario(
                        nombre=data.get("nombre", "Desconocido"),
                        apellido=data.get("apellido", "Desconocido"),
                        email=data.get("email", "Desconocido"),
                        genero=data.get("genero", "Desconocido"),
                    )

                    # Añadir la instancia creada a la lista de usuarios
                    usuarios.append(usuario)

                except json.JSONDecodeError as e:
                    log_error(f"Error al decodificar JSON: {e} - Línea: {line}")
                except TypeError as e:
                    log_error(f"Error de tipo al crear Usuario: {e} - Línea: {line}")
                except KeyError as e:
                    log_error(f"Error de clave faltante: {e} - Línea: {line}")
                except Exception as e:
                    log_error(f"Error inesperado: {e} - Línea: {line}")

    except FileNotFoundError as e:
        log_error(f"Archivo usuarios.txt no encontrado: {e}")
    except Exception as e:
        log_error(f"Error al leer el archivo usuarios.txt: {e}")

    # Imprimir los datos de los usuarios
    for usuario in usuarios:
        print(usuario.nombre, usuario.apellidos, usuario.email, usuario.genero)


def log_error(message):
    # Registrar el mensaje de error en error.log
    with open("error.log", "a") as error_file:
        error_file.write(message + "\n")


if __name__ == "__main__":
    main()

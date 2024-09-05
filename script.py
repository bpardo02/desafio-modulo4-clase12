# script.py
import os
from usuario import Usuario

def crear_instancias_usuarios(archivo_usuarios, archivo_errores):
    usuarios = []
    if os.path.exists(archivo_usuarios):
        with open(archivo_usuarios, 'r') as file:
            for linea in file:
                try:
                    datos_usuario = linea.strip().split(',')
                    if len(datos_usuario) != 4:
                        raise ValueError("Formato de línea incorrecto")
                    nombre, apellido, email, genero = datos_usuario
                    usuario = Usuario(nombre, apellido, email, genero)
                    usuarios.append(usuario)
                except Exception as e:
                    with open(archivo_errores, 'a') as error_log:
                        error_log.write(f"Error al procesar la línea: {linea}\n")
                        error_log.write(f"Excepción: {e}\n")
    else:
        print(f"El archivo {archivo_usuarios} no existe.")
    return usuarios

if __name__ == "__main__":
    archivo_usuarios = 'usuarios.txt'
    archivo_errores = 'error.log'
    usuarios = crear_instancias_usuarios(archivo_usuarios, archivo_errores)
    for usuario in usuarios:
        print(f"Usuario creado: {usuario.nombre} {usuario.apellidos}, Email: {usuario.email}, Género: {usuario.genero}")

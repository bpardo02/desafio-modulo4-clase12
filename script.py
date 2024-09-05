import os
import json
from usuario import Usuario

def crear_instancias_usuarios(archivo_usuarios, archivo_errores):
    usuarios = []
    if os.path.exists(archivo_usuarios):
        with open(archivo_usuarios, 'r') as f:
            for linea in f:
                try:
                    # Intentar cargar la línea como JSON
                    datos_usuario = json.loads(linea.strip())
                    # Validar que todos los campos necesarios estén presentes
                    if not all(k in datos_usuario for k in ("nombre", "apellido", "email", "genero")):
                        raise ValueError("Faltan campos en la línea")
                    usuario = Usuario(**datos_usuario)
                    usuarios.append(usuario)
                except Exception as e:
                    with open(archivo_errores, 'a') as error_log:
                        error_log.write(f"Error al procesar la línea: {linea}\n")
                        error_log.write(f"Excepción: {e}\n")
                    print(f"Error al procesar la línea: {linea}")
                    print(f"Excepción: {e}")
    else:
        print(f"El archivo {archivo_usuarios} no existe.")
    return usuarios

if __name__ == "__main__":
    archivo_usuarios = 'usuarios.txt'
    archivo_errores = 'error.log'
    usuarios = crear_instancias_usuarios(archivo_usuarios, archivo_errores)
    for usuario in usuarios:
        print(f"Usuario creado: {usuario.nombre} {usuario.apellidos}, Email: {usuario.email}, Género: {usuario.genero}")

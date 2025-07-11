import tkinter as tk
from tkinter import ttk
""" hola """
def seleccionar_usuario_gui():
    """
    Muestra una ventana con un combobox para seleccionar un usuario.
    """
    def mostrar_seleccion():
        seleccion = combo.get()
        if seleccion:
            print(f"Usuario seleccionado: {seleccion}")
            ventana.destroy()  # Cierra la ventana después de la selección
        else:
            print("Por favor, selecciona un usuario.")

    ventana = tk.Tk()
    ventana.title("Seleccionar Usuario")

    etiqueta = ttk.Label(ventana, text="Selecciona un usuario:")
    etiqueta.pack(pady=10)

    usuarios = ["Alice", "Bob", "Charlie", "David"]
    combo = ttk.Combobox(ventana, values=usuarios, state="readonly")
    combo.pack(pady=5)
    combo.set(usuarios[0])  # Establece una selección por defecto

    boton_seleccionar = ttk.Button(ventana, text="Seleccionar", command=mostrar_seleccion)
    boton_seleccionar.pack(pady=10)

    ventana.mainloop()

# Ejemplo de uso
seleccionar_usuario_gui()

import csv
import datetime
import os

# --- Configuración ---
NOMBRE_ARCHIVO = 'registro_llamadas_cfe.csv'
CABECERAS = ['Fecha y Hora', 'Ejecutvo', 'Nombre de titular', 'Numero de telefono', 'ID de Monedero', 'Folio de monedero', 'Tipo de Consulta', 'Estatus', 'Notas Adicionales']
# Opciones para tipificar la llamada
TIPOS_LLAMADA = [
    "Consulta de saldo",
    "Consulta de NIP",
    "Error al realizar compra online",
    "Error al realizar compra en sucursal",
    "Cargo doble o triple",
    "Informacion de sucursales",
    "seguimiento a pedido",
    "reemplazo",
    "Asesoría sobre sucursales físicas y en línea",
    "Vigencia",
    "levantar reporte",
    "Bloqueo de tarjeta por robo o extravío"
]

# Opciones para el estatus de la llamada
ESTATUS_LLAMADA = [
    "Por resolver",
    "Resuelto"
]

def inicializar_csv():
    """
    Verifica si el archivo CSV existe. Si no, lo crea y escribe las cabeceras.
    """
    if not os.path.exists(NOMBRE_ARCHIVO):
        print(f"Archivo '{NOMBRE_ARCHIVO}' no encontrado. Se creará uno nuevo.")
        with open(NOMBRE_ARCHIVO, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerow(CABECERAS)

def obtener_opcion_valida(prompt, opciones):
    """
    Muestra una lista de opciones y solicita al usuario que elija una válida.
    """
    print(prompt)
    for i, opcion in enumerate(opciones, 1):
        print(f"  {i}. {opcion}")

    while True:
        try:
            eleccion = int(input("Selecciona una opción (número): "))
            if 1 <= eleccion <= len(opciones):
                return opciones[eleccion - 1]
            else:
                print("Error: Opción no válida. Por favor, elige un número de la lista.")
        except ValueError:
            print("Error: Debes introducir un número.")

def registrar_llamada():
    """
    Captura los datos de una nueva llamada y los guarda en el archivo CSV.
    """
    print("\n--- Nuevo Registro de Llamada ---")

    # 1. Obtener numero de telefono
    id_telefono = input("Telefono: ")

    # 2. Obtener nombre
    id_nombre = input("Nombre: ")

    # 3. Obtener ID del Monedero
    id_monedero = input("16 digitos de monedero Club: ")

    # 4. Obtener folio 
    id_folio = input("Folio: ")

    # 5. Obtener Tipo de Consulta
    tipo_consulta = obtener_opcion_valida("\nSelecciona el tipo de consulta:", TIPOS_LLAMADA)

    # 6. Obtener Notas adicionales
    notas = input("Añade notas adicionales (o presiona Enter para dejar en blanco): ")

    # 7. Obtener Estatus de la llamada
    estatus = obtener_opcion_valida("\nSelecciona el estatus de la llamada:", ESTATUS_LLAMADA)

    # 8. Obtener fecha y hora actual
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 9. Crear la fila de datos y guardarla
    fila = [timestamp, id_telefono, id_nombre, id_monedero, id_folio, tipo_consulta, estatus, notas]
    
    with open(NOMBRE_ARCHIVO, mode='a', newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(fila)

    print("\n¡Llamada registrada con éxito!")
    print("-" * 30)


def main():
    """
    Función principal de la aplicación.
    """
    # Asegurarse de que el archivo CSV esté listo
    inicializar_csv()
    
    print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
    print("   Bienvenido al Sistema de Registro de Llamadas      ")
    print("               〰 El club 〰                      ")
    print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")

    while True:
        registrar_llamada()
        
        # Preguntar si se desea continuar
        continuar = input("\n¿Deseas registrar otra llamada? (s/n): ").lower()
        if continuar != 's':
            break
            
    print("\nGracias por registrar tu llamada. ¡Hasta luego! ")


# Punto de entrada para ejecutar la aplicación
if __name__ == "__main__":
    main()

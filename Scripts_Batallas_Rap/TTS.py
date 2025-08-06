import os
import tkinter as tk
from tkinter import filedialog, Scale, StringVar, OptionMenu, messagebox
import pyttsx3

# =====================================================================
#                          FUNCIONES PRINCIPALES
# =====================================================================

# Variable global para el motor pyttsx3, para inicializarlo una sola vez
global_engine = None

def inicializar_motor():
    """Inicializa el motor de pyttsx3 una sola vez."""
    global global_engine
    if global_engine is None:
        try:
            global_engine = pyttsx3.init()
            return global_engine
        except Exception as e:
            messagebox.showerror("Error de Inicialización", f"No se pudo inicializar el motor de voz: {e}\nPor favor, asegúrate de tener un motor TTS instalado en tu sistema (ej. voces de Microsoft en Windows, eSpeak/NSSpeechSynthesizer en Linux/macOS).")
            return None
    return global_engine

def obtener_voces_disponibles():
    """
    Obtiene la lista de IDs de voces disponibles en el sistema.
    """
    engine = inicializar_motor()
    if engine:
        voices = engine.getProperty('voices')
        return [voice.id for voice in voices]
    return []

def convertir_texto_a_voz_y_guardar(texto, voz_seleccionada, velocidad, ruta_guardado):
    """
    Convierte un texto a voz usando pyttsx3, lo guarda en un archivo y lo reproduce.
    """
    engine = inicializar_motor()
    if not engine: # Si el motor no se pudo inicializar
        return

    try:
        # Detener cualquier reproducción previa para asegurar que la nueva se procese
        engine.stop()

        # Seleccionar la voz deseada
        engine.setProperty('voice', voz_seleccionada)

        # Ajustar la velocidad de reproducción
        engine.setProperty('rate', velocidad)

        # Guardar el audio en el archivo especificado
        engine.save_to_file(texto, ruta_guardado)
        engine.runAndWait() # Esto ejecuta el proceso de guardado y reproduce el audio

        messagebox.showinfo("Éxito", f"Archivo de audio guardado exitosamente en:\n{ruta_guardado}")
        print(f"Archivo de audio guardado exitosamente en: {ruta_guardado}")

    except Exception as e:
        messagebox.showerror("Error de Conversión/Guardado", f"Ocurrió un error al convertir o guardar el audio: {e}")
        print(f"Error de Conversión/Guardado: {e}")

def seleccionar_archivo_txt_y_audio_destino():
    """
    Permite al usuario seleccionar un archivo de texto y luego la ubicación para guardar el audio.
    """
    # 1. Seleccionar el archivo de texto de entrada
    ruta_archivo_txt = filedialog.askopenfilename(
        title="1. Seleccionar archivo de texto (.txt)",
        filetypes=[("Archivos de texto", "*.txt")]
    )
    if not ruta_archivo_txt: # Si el usuario cancela la selección de TXT
        etiqueta_ruta_txt.config(text="Ningún archivo TXT seleccionado.")
        return

    etiqueta_ruta_txt.config(text=f"TXT seleccionado: {os.path.basename(ruta_archivo_txt)}")

    try:
        with open(ruta_archivo_txt, "r", encoding="utf-8") as archivo:
            texto_para_procesar = archivo.read()

        if not texto_para_procesar.strip():
            messagebox.showwarning("Advertencia", "El archivo de texto está vacío. No hay contenido para convertir.")
            etiqueta_ruta_txt.config(text="Archivo TXT vacío. Selecciona otro.")
            return

        # 2. Pedir al usuario dónde guardar el archivo de audio de salida
        ruta_guardado_audio = filedialog.asksaveasfilename(
            title="2. Guardar audio como...",
            defaultextension=".wav", # pyttsx3 suele generar WAV. Para MP3, se necesitaría conversión adicional.
            filetypes=[("Archivos de Audio WAV", "*.wav"), ("Todos los archivos", "*.*")] # MP3 requiere ffmpeg y pydub
        )
        if not ruta_guardado_audio: # Si el usuario cancela el guardado del audio
            etiqueta_ruta_txt.config(text="Guardado de audio cancelado.")
            return

        # 3. Obtener las configuraciones de voz y velocidad
        voz_seleccionada = seleccion_voz.get()
        velocidad_actual = velocidad_slider.get()

        # 4. Iniciar la conversión y guardado
        convertir_texto_a_voz_y_guardar(texto_para_procesar, voz_seleccionada, velocidad_actual, ruta_guardado_audio)

    except FileNotFoundError:
        messagebox.showerror("Error de Archivo", f"El archivo '{ruta_archivo_txt}' no fue encontrado.")
    except Exception as e:
        messagebox.showerror("Error General", f"Ocurrió un error inesperado al procesar: {e}")

# =====================================================================
#                          CONFIGURACIÓN DE LA GUI
# =====================================================================

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Convertir Texto a Audio (Telo-Enviamos Studio)")
ventana.geometry("550x500") # Tamaño inicial de la ventana
ventana.resizable(False, False) # Desactivar redimensionamiento para simplificar el layout

# Frame principal para organizar los widgets
frame_principal = tk.Frame(ventana, padx=25, pady=25)
frame_principal.pack(expand=True, fill="both")

# Título de la Aplicación
titulo = tk.Label(frame_principal, text="Generador de Audio desde Texto", font=("Helvetica", 20, "bold"), fg="#333333")
titulo.pack(pady=10)

# Descripción
descripcion = tk.Label(frame_principal, text="Convierte tu texto en audio, ideal para podcasts o demos.", wraplength=480, font=("Helvetica", 10), fg="#555555")
descripcion.pack(pady=5)

# Etiqueta para mostrar el nombre del archivo TXT seleccionado
etiqueta_ruta_txt = tk.Label(frame_principal, text="Ningún archivo TXT seleccionado", wraplength=480, font=("Helvetica", 10, "italic"), fg="#777777")
etiqueta_ruta_txt.pack(pady=10)

# Botón para seleccionar archivo TXT y iniciar el proceso de guardado/conversión
boton_procesar = tk.Button(frame_principal, text="Procesar Texto a Audio", command=seleccionar_archivo_txt_y_audio_destino,
                            font=("Helvetica", 14, "bold"), bg="#007BFF", fg="white", relief="raised", padx=15, pady=8)
boton_procesar.pack(pady=20, ipadx=10, ipady=5)

# Separador visual
tk.Frame(frame_principal, height=2, bd=1, relief="sunken").pack(fill="x", padx=10, pady=15)


# =====================================================================
# SECCIÓN DE SELECCIÓN DE VOZ
# =====================================================================
label_voz = tk.Label(frame_principal, text="Configuración de Voz:", font=("Helvetica", 12, "bold"), fg="#333333")
label_voz.pack(pady=5)

opciones_voces = obtener_voces_disponibles()
if not opciones_voces:
    opciones_voces = ["No se encontraron voces disponibles (Verifica tu sistema)"]
    # El warning ya se mostró al inicializar el motor si es el caso

seleccion_voz = StringVar(ventana)
if opciones_voces:
    seleccion_voz.set(opciones_voces[0]) # Establecer la primera voz como predeterminada si hay opciones

menu_voces = OptionMenu(frame_principal, seleccion_voz, *opciones_voces)
menu_voces.config(font=("Helvetica", 10), width=60, bg="#F0F0F0")
menu_voces.pack(pady=5)

# =====================================================================
# SECCIÓN DE AJUSTE DE VELOCIDAD
# =====================================================================
label_velocidad = tk.Label(frame_principal, text="Ajusta la Velocidad de Habla:", font=("Helvetica", 12, "bold"), fg="#333333")
label_velocidad.pack(pady=15)

velocidad_slider = Scale(frame_principal, from_=50, to=300, orient="horizontal", label="Velocidad (palabras por minuto)", length=400, resolution=10, font=("Helvetica", 9), fg="#555555", troughcolor="#E0E0E0")
velocidad_slider.set(175) # Valor predeterminado (un poco más natural que 200 a veces)
velocidad_slider.pack(pady=5)

# =====================================================================
# INICIAR APLICACIÓN
# =====================================================================
# Inicializar el motor al inicio de la aplicación para que las voces estén cargadas
inicializar_motor()

ventana.mainloop()
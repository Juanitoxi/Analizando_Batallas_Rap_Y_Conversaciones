# Analizando Batallas Rap Y Conversaciones

Desarrollar la habilidad para transcribir es de las más importantes a la hora de analizar tendencias y emociones, aquí aprenderás cómo evolucionan las herramientas para crear informes, gráficos y visualizaciones

<img width="1280" height="720" alt="Muchos hablan (2)" src="https://github.com/user-attachments/assets/7457cff6-ee7d-48da-bfa0-bc6537a25c26" />


## 📁 Estructura de Carpetas Propuesta

```
Analizando_Batallas_Rap_Y_Conversaciones/
│
├── 📁 src/                          # Código fuente principal
│   ├── 📁 core/                     # Funcionalidades centrales
│   │   ├── Ventana_Asistente.py     # Script principal con GUI
│   │   
│   │
│   ├── 📁 analysis/                 # Módulos de análisis
│   │   ├── Union_Gramatical.py         # Análisis gramatical concentrado en excel  
│   │   ├── N-Gramas.py                 #Determinar repetición de patrones
│   │   └── Seguim_Palabras.py          # Seguimiento de palabras
│   │
│   ├── 📁 visualization/            # Visualización de datos
│   │   ├── Graficos_Palabras.py    # Gráficos de palabras
│   │   ├──  
│   │   └── Terminacion_Grafica.py  # Gráficos de terminación
│   │
│   └── 📁 media/                    # Procesamiento multimedia
│       ├── Video_Audio.py          # Procesamiento de video/audio
│       └── TTS.py                  # Text-to-Speech
│
├── 📁 docs/                         # Documentación
│   ├── README.md
│   

├── requirements.txt                 # Dependencias del proyecto
├── .gitignore                      # Archivos a ignorar
└── LICENSE                         # Licencia del proyecto
```

## 📋 Archivos que Mover

### Módulo Core (src/core/)
- `Ventana_Asistente.py` → **MANTENER AQUÍ** (script principal)

### Módulo Analysis (src/analysis/)
- `N-Gramas.py`
- `Seguim_Palabras.py`
- `Union_Gramatical.py`

### Módulo Visualization (src/visualization/)
- `Graficos_Palabras.py`
- `Terminacion_Grafica.py`

### Módulo Media (src/media/)
- `Video_Audio.py`
- `TTS.py`

### Tests
Se pueden hacer infinidad de pruebas, ya sea para analizar todo un discurso

## 🔧 Archivos a Crear

### requirements.txt
```
tkinter
subprocess32
matplotlib
numpy
pandas
nltk
speechrecognition
pyttsx3
opencv-python
```


## 📝 README.md 

<img width="306" height="368" alt="image" src="https://github.com/user-attachments/assets/68483f3d-594e-4ecc-b1ed-b14ae978dc7f" />

```markdown
# Analizando Batallas Rap Y Conversaciones




## 🚀 Características

  <STT = Speech To Text>
  <TTS = Text To Speech>

- **Transcripción Automática STT**: Convierte video a audio
- **Transcripción Automática STT**: Convierte audio a texto
- **Transcripción Automática TTS **: Convierte texto a audio
- **Análisis de N-gramas**: Identifica patrones lingüísticos
- **Visualización de Datos**: Gráficos y estadísticas usando Matplotlib
- **Interfaz Gráfica**: GUI intuitiva con Tkinter
- **Procesamiento en Lote**: Ejecuta múltiples análisis



## 🛠️ Instalación

```
1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/Analizando_Batallas_Rap_Y_Conversaciones.git
cd Analizando_Batallas_Rap_Y_Conversaciones
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
python src/core/Ventana_Asistente.py
```

## 📖 Uso

<img width="592" height="290" alt="image" src="https://github.com/user-attachments/assets/6ccaa325-1e51-41c6-863f-2dce271f82c4" />

El script principal `Ventana_Asistente.py` funciona como un carrusel que ejecuta los diferentes módulos en orden:

1. **Comienza con Video-Audio-Texto** (depende de la situación)
2. **Análisis lingüístico** ( Union_Gramatical.py) #una vez tengas texto hay que usar este script para transformarlo en un .xlsx
3. **Generación de gráficos** (Graficos_Palabras.py) #se pueden graficar terminaciones )
4. **Exportación de resultados** (todo en excel y listo para png para subir a redes)

## 🏗️ Arquitectura

```
GUI (Tkinter) → Subprocess → Módulos Específicos → Resultados
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Distribuido bajo la Licencia un Analista de Datos Especializado en Automatizaciones.



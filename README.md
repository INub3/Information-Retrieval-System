# Proyecto RI - B1

## 🎯 Sistema de Recuperación de Información Interactivo

Sistema completo para comparar modelos clásicos y modernos de recuperación de información.

### 📦 Estructura del Proyecto

```
.
├── proyectoB1.ipynb          # Notebook principal con análisis e interfaz interactiva
├── requirements.txt          # Dependencias del proyecto
├── sources/                  # Módulos de recuperación de información
│   ├── prepro_func.py       # Preprocesamiento (tokenización, stemming, TF-IDF)
│   ├── bm25_model.py        # Modelo BM25
│   ├── jaccard_similarity.py # Similitud Jaccard (vectores binarios)
│   └── __init__.py          # Inicializador del paquete
├── data/                     # Corpus de documentos (archivos CSV)
└── README.md                 # Este archivo
```

### 🚀 Instalación Rápida

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutar el notebook:**
   ```bash
   jupyter notebook proyectoB1.ipynb
   ```

### 🔍 Modelos Implementados

1. **Jaccard** - Similitud de Jaccard con vectores binarios
   - Usa presencia/ausencia de términos
   - Fórmula: |A ∩ B| / |A ∪ B|

2. **TF-IDF** - Term Frequency-Inverse Document Frequency
   - Similitud coseno entre vectores TF-IDF
   - Pondera términos raros como más importantes

3. **BM25** - Best Matching 25
   - Modelo probabilístico de recuperación
   - Considere la frecuencia del término y la longitud del documento

### 🎨 Interfaz Interactiva

**En la última sección del notebook `proyectoB1.ipynb`:**

- **Entrada de búsqueda:** Campo de texto para ingresar tu consulta
- **Selector Top K:** Elige cuántos resultados deseas (1-20)
- **Botones de modelos:**
  - 🔍 **Jaccard** - Ver resultados con similitud Jaccard
  - 📊 **TF-IDF** - Ver resultados con TF-IDF
  - 🎯 **BM25** - Ver resultados con BM25
  - ⚖️ **Comparar** - Ver los 3 modelos lado a lado
  - 🗑️ **Limpiar** - Limpiar búsqueda y resultados

### 📊 Flujo de Ejecución

1. Ejecuta las celdas secuencialmente hasta el final
2. Se cargarán automáticamente:
   - Corpus de 23 archivos CSV (11,500+ documentos)
   - Índice invertido
   - Matriz TF-IDF
   - Índice BM25

3. En la interfaz interactiva:
   - Ingresa un término o frase
   - Haz clic en un botón para buscar
   - Los resultados mostrarán rank, score, título del trabajo y empresa

### 💻 Requisitos Técnicos

- **Python:** >= 3.8
- **Librerías principales:**
  - `pandas` - Manipulación de datos
  - `nltk` - Procesamiento de lenguaje natural
  - `scikit-learn` - Machine learning utilities
  - `ipywidgets` - Interfaz interactiva en Jupyter
  - `jupyter` - Notebook interactivo

### 📝 Corpus de Datos

El proyecto trabaja con un corpus de ofertas de empleo de 23 categorías de ingeniería:
- Administración de Empresas
- Agroindustria
- Ciencia de Datos
- Ingeniería Civil
- Ingeniería de Software
- Inteligencia Artificial
- ... y más

Cada documento incluye: ID, título, empresa, carreras requeridas, descripción

### 🔧 Funciones Principales

**En `sources/prepro_func.py`:**
- `tokenize()` - Tokenización en español
- `remove_special_characters()` - Limpieza de caracteres
- `stemming_tokens()` - Reducción a raíz de palabras
- `build_tfidf_matrix()` - Construcción de matriz TF-IDF
- `score_queries_tfidf()` - Scoring de queries con TF-IDF

**En `sources/bm25_model.py`:**
- `build_bm25_index()` - Construcción del índice BM25
- `bm25_score_doc()` - Scoring de documento individual
- `score_queries_bm25()` - Scoring de múltiples queries

**En `sources/jaccard_similarity.py`:**
- `binary_vector_jaccard()` - Similitud Jaccard binaria
- `jaccard_rank()` - Ranking con Jaccard

### 📚 Ejemplo de Uso

```python
# Una vez ejecutadas todas las celdas del notebook

# Buscar con interfaz
# Ingresa: "inteligencia artificial"
# Haz clic: ⚖️ Comparar
# Verás resultados de los 3 modelos

# Resultado esperado:
# - Top 5 documentos más relevantes por cada modelo
# - Scores normalizados entre 0 y 1
# - Título del trabajo, empresa, y preview
```

### 🎓 Objetivos del Proyecto

- ✅ Comparar modelos clásicos de RI (Jaccard, TF-IDF, BM25)
- ✅ Construcción de índice invertido
- ✅ Procesamiento de lenguaje natural en español
- ✅ Interfaz interactiva para consultas
- ✅ Recuperación semántica con embeddings
- ✅ Evaluación con métricas (Precision, Recall, MAP)

### 📄 Notas

- El notebook es completamente reproducible
- Los modelos trabajan en memoria (no requieren bases de datos externas)
- El tiempo de ejecución depende del tamaño del corpus (primero: ~30-60 seg)
- Ideal para análisis educativo y comparación de modelos

---
**Autor:** Leandro Bravo, Michael Enríquez y Aubertin Ochoa
**Fecha:** Mayo 2026  
**Curso:** Recuperación de Información

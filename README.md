# 📊 Anime Analytics: Tendencias, Calidad y Evolución de la Industria del Anime en las Últimas Dos Décadas

## Un análisis profundo basado en datos de MyAnimeList utilizando pipelines automatizados y visualización avanzada.

Este proyecto desarrolla un sistema completo de análisis de datos centrado en la industria del anime, utilizando información pública obtenida a través de Jikan API (wrapper de MyAnimeList).
El objetivo es identificar patrones de calidad, popularidad y producción a lo largo del tiempo, evaluar el desempeño de estudios y géneros, y comprender la evolución general del anime en las últimas dos décadas.

El proyecto incluye un pipeline automatizado de extracción y limpieza de datos, análisis exploratorio avanzado, modelado estadístico ligero, y un dashboard interactivo que presenta hallazgos clave para stakeholders de la industria del entretenimiento, distribuidores, plataformas de streaming y estudios.

---

## 📚 Tabla de Contenidos

- [🎯 Propósito](#-propósito)
- [📦 Conjunto de Datos](#-conjunto-de-datos)
- [🧪 Desarrollo del Proyecto](#-desarrollo-del-proyecto)
- [💡 Insights claves](#-insights-claves)
- [🛠️ Tecnologías](#️-tecnologías)
- [⚙️ Instalación](#️-instalación)
- [👤 Autor](#-autor)

---

## 🎯 Propósito
* Evaluar tendencias en calidad y popularidad del anime a lo largo del tiempo.
* Determinar qué factores influyen más en el éxito de un anime (estudio, temporada, género, episodios, duración).
* Comparar el desempeño entre estudios de animación.
* Identificar patrones estacionales y picos de producción.
* Facilitar decisiones basadas en datos para plataformas que licenciaron anime, estudios de doblaje o marketing.

---

## 📦 Conjunto de Datos

El conjunto de datos utilizado contiene las siguientes columnas:

1.-Tabla animes:
- `mal_id`: ID de MyAnimeList
- `titulo`: Título del anime
- `tipo`: Tipo de anime ("TV","OVA","Movie","Special","ONA","Music")
- `episodios`: Número de episodios
- `annio`: Año
- `temporada`: Temporada (Enum,"summer","winter","spring","fall")
- `clasificacion`: Clasificación de audiencia de anime ("G - All Ages""PG - Children","PG-13 - Teens 13 or older","R - 17+ (violence & profanity)","R+ - Mild Nudity","Rx - Hentai")
- `duracion`: Duración bruta analizada
- `sinopsis`: Sinopsis
- `anime_rank`: Clasificación/Categoria

2.-Tabla generos:
- `genero_id`: ID MyAnimeList
- `nombre_genero`: Nombre de genero

3.-Tabla estudios:
- `estudio_id`: ID MyAnimeList
- `nombre_estudio`: Nombre del estudio
- `favoritos`: Los favoritos de los miembros de los prouctores
- `establecido`: Fecha de establecimiento

4.-Tabla popularidad:
- `mal_id`:
- `score`:
- `scored_by`:
- `miembros`:
- `favoritos`:
- `popularidad`:

5.-Tabla anime_generos:
- `mal_id`:
- `genero_id`:

6.-Tabla anime_estudios:
- `mal_id`:
- `estudio_id`:

Fuente: [Nombre de la fuente o “datos simulados/ficticios”].

---

## 🧪 Desarrollo del Proyecto

1. **Carga y exploración inicial de los datos**:
   - Exploración básica con `.head()`, `.info()`, `.describe()`, etc.

2. **Limpieza y preprocesamiento**:
   - Manejo de valores nulos, duplicados, formatos y conversiones de fechas.

3. **Análisis exploratorio de datos (EDA)**:
   - [Ej. Distribución, correlaciones, agrupaciones, etc.]

4. **Visualización de datos**:
   - Uso de gráficos de barras, líneas, cajas, dispersión y mapas de calor.

5. **Modelado o reportes (opcional)**:
   - [Si aplica: modelos de ML, clustering, predicciones, etc.]

6. **Conclusiones y recomendaciones**:
   - Síntesis de hallazgos clave y propuestas de acción.

---

## 💡 Insights claves

- [Insight 1]
- [Insight 2]
- [Recomendación práctica o estratégica basada en los datos]

---

## 🛠️ Tecnologías

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook / Google Colab
- [Otras herramientas que uses, como Scikit-learn, Plotly, etc.]

---

## ⚙️ Instalación

### 1. Clonar este repositorio:
```bash
git clone https://github.com/tu_usuario/nombre_del_proyecto.git
```
### 2. Uso de un Entorno Virtual para Aislar Dependencias

Para evitar conflictos con versiones de librerías, se recomienda usar entornos virtuales.

####  Crear y Activar un Entorno Virtual

##### Crear el entorno virtual:
```
python -m venv venv
```
##### Activar el entorno:
* #### En Windows:

    ```
    venv\Scripts\activate
    ```

* #### En Mac/Linux::

    ```
    source venv/bin/activate
    ```
#### 3. Instalar dependencias dentro del entorno:
* #### Opición 1:
    ```
    pip install -r requirements.txt
    ```

* #### Opción 2 (De forma manual):
    ```
    pip install numpy pandas matplotlib seaborn scikit-learn
    ```

---

## 👤 Autor

**Said Mariano Sánchez** – *smariano170@gmail.com*  
Este proyecto forma parte de mi portafolio como analista de datos Jr.

---

## 📝 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. Puedes usarlo, modificarlo y distribuirlo libremente, siempre que menciones al autor original.

---
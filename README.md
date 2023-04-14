
PROYECTO INDIVIDUAL Nº1
Machine Learning Operations (MLOps)

Alumno: Francisco Jiménez de Aréchaga
Cuenta Github: bigtimingme
Repositorio: MLOps_09

CONSIGNAS:

1. Hacer las siguientes transformaciones a los archivos csv de las plataformas de streaming (realizado en el archivo ETL.ipynb):

  Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123).

  Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”).

  De haber fechas, deberán tener el formato AAAA-mm-dd.

  Los campos de texto deberán estar en minúsculas, sin excepciones.

  El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas).


2. Desarrollar una API con las siguientes consultas (hecho en la carpeta soyhenry-fastapi):

  Película con mayor duración con filtros AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (función: get_max_duration(year, platform, duration_type)).

  Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (función: get_score_count(platform, scored, year)).

  Cantidad de películas por plataforma con filtro de PLATAFORMA. (función: get_count_platform(platform)).

  Actor que más se repite según plataforma y año. (función: get_actor(platform, year)).

  Cantidad de contenido por que se produció en un determinado país en un año. (función: prod_per_country(type,country,year)).

  Cantidad de contenido total según el rating dado por las reseñas de los usuarios. (función: get:contents(rating)).

3. Hacer un Deployment de la API del punto 2:
  El deployment del sistema de recomendación está en https://github.com/bigtimingme/MLOps_09

4. Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA):
  No encontré relaciones interesantes, salvo que el promedio de reseñas está entre 3,3 y 3,8.

5. Sistema de recomendación:
El sistema de recomendación que creé es un sistema basado en la combinación de la columna title(título) y la columna listed_in(géneros). Usé luego CountVectorizer y cosine_similarity de la librería scikit-learn para crear una matrix de similitud.
Al ser imperativo la inclusión del sistema de recomendación en el script de la API, creé una columna en el DataFrame de las consultas que se llama 'recommender' y puse los 5 títulos más recomendados en orden descendente para cada item.

6. Video: 
  Hacer un video mostrando el resultado de las consultas propuestas y del modelo de ML entrenado.
  link al video:


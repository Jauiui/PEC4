# Análisis de la Población y Uso de Armas de Fuego en Estados Unidos

Este proyecto tiene como objetivo repasar anterores ejercicios de la asignatura de una forma diversa, mediante el estudio del mercado en relación a la población estadounidense respecto al uso de armas de fuego. Los datos utilizados tienen relacion con los permisos concedidos de armas, su solicitud para pistolas o armas largas, así como los estados en donde se situan dichos datos y una representación de numero de habitantes de cada estado (2014).

## Estructura del Proyecto

- `read_and_clean.py`: Funciones para la lectura y limpieza de los datos (Ej 1).
- `data_procesing.py`: Funciones para el procesamiento de los datos (Ej 2).
- `data_clustering.py`: Funciones para el análisis de los datos (año y estado donde se encontraron mayor numero de armas de cada tipo) (Ej 3).
- `visualization.py`: Funciones para la visualización de datos en una gráfica y su interpretación (permit, hand_gun y long_gun registrado por cada uno de los años) (Ej 4).
- `state_analysis.py`: Funciones para armar un nuevo dataframe y realizar un análisis (calcular valores relativos y profundizar en los valores atípicos o outliers) (Ej 5).
- `choropleth_maps.py`: Funciones para poder extraer imágenes geográficas informativas (pintados según los valores de permit_perc, handgun_perc y longgun_perc cada vez) (Ej 6).
- `requirements.txt`: Dependencias necesarias para ejecutar el proyecto.
- `LICENSE`: Licencia del proyecto.
- `README.md`: Este archivo.

También encontramos los test para cada uno de los archivos .py del proyecto.

## Instalación

1. Clona este repositorio:
    ```sh
    git clone PONER EL LINK
    ```

2. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta el script principal:
    ```sh
    python3 main.py --all
    ```
2. Si se quieren ejecutar sctipts separados se debe de sustituir --all por el nombre la función a ejecutar:
    ```sh
    python3 main.py --read_csv2
    ```

3. Para ejecutar las pruebas:
    ```sh
    python3 -m unittest discover
    ```

## Estructura de Datos

- `nics-firearm-background-checks.csv`: Dataset principal con información sobre verificaciones de antecedentes para permisos de armas.
- `us-state-populations.csv`: Dataset con información de población de los estados de Estados Unidos en 2014.

## Funciones Principales

### Análisis de Datos

- `read_csv(url)`: Lee el archivo CSV y devuelve un DataFrame.
- `rename_col(df)`: Renombra la columna `longgun` a `long_gun`.
- `clean_csv(df)`: Limpia el DataFrame eliminando columnas no necesarias.
- `breakdown_date(df)`: Divide la columna `month` en dos columnas `year` y `month`.
- `erase_month(df)`: Elimina la columna `month`.
- `groupby_state_and_year(df)`: Agrupa los datos por estado y año.
- `print_biggest_handguns(grouped_df)`: Imprime el estado y año con más solicitudes de pistolas.
- `print_biggest_longguns(grouped_df)`: Imprime el estado y año con más solicitudes de armas largas.
- `groupby_state(grouped_df)`: Agrupa los datos por estado.
- `clean_states(grouped_df)`: Elimina los estados Guam, Mariana Islands, Puerto Rico y Virgin Islands del DataFrame.
- `read_csv2(url)`: Lee el archivo CSV y devuelve un DataFrame.
- `merge_datasets(cleaned_df, df2)`: Fusiona dos DataFrames en uno.
- `calculate_relative_values(merged_df)`: Calcula los valores relativos de permisos, pistolas y armas largas.
- `analyze_kentucky_outlier(merged_df)`: Hace una comparación entre las medias antes y después de la imputación de los datos de para el porcentaje de permisos del estado de Kentuky.
- `open_json(url)`: Lee el archivo "FeatureCollection" y devuelve un archivo.json de tipo FeatureCollection.
- `create_choropleth(merged_df, state_geo, column)`: Crea un mapa de coropletas basado en los datos proporcionados.
- `create_image(merged_df, state_geo, column1, column2, column3)`: Crea y guarda imágenes de mapas de coropletas para tres columnas diferentes.

### Visualización de Datos

- `time_evolution(df)`: Genera un gráfico de evolución temporal de permisos, pistolas y largas.

## Correcciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio.

## Licencia

Este proyecto está bajo la Licencia unlicense. Consulta el archivo [LICENSE]para más detalles.

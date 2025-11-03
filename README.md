# Informe de Análisis: Dataset de Suicidios en Antioquia (2005-2024)

# 1. Descripción General del Dataset

**Nombre**: Suicidios en Antioquia (2005-2024)
**Fuente**: Secretaría de Salud y Protección Social Departamental de Antioquia
**Dimensiones**: 2,500 registros × 10 variables
**Período temporal**: 2005-2024 (20 años)
**Cobertura geográfica:** 125 municipios distribuidos en 9 regiones de Antioquia
**Archivo:** suicidios-en-antioquia.csv

**Descripción:** Este dataset contiene registros oficiales de casos de suicidio en todos los municipios de Antioquia durante dos décadas. Cada registro representa la información anual de un municipio específico, incluyendo datos poblacionales, geográficos y el número de casos registrados.

## 2. Clasificación de Columnas por Tipo

| Columna                   | Tipo Original | Tipo Final | Clasificación          | Descripción                               |
| ------------------------- | ------------- | ---------- | ---------------------- | ----------------------------------------- |
| `NombreMunicipio`         | object        | object     | **Texto**              | Nombre del municipio                      |
| `CodigoMunicipio`         | int64         | int64      | **Numérica (entera)**  | Código único del municipio                |
| `Ubicación`               | object        | object     | **Texto**              | Coordenadas geográficas (formato POINT)   |
| `NombreRegion`            | object        | category   | **Categórica Nominal** | Región de Antioquia (9 categorías)        |
| `CodigoRegion`            | int64         | int64      | **Numérica (entera)**  | Código numérico de la región              |
| `Anio`                    | int64         | int64      | **Numérica (entera)**  | Año del registro (2005-2024)              |
| `CausaMortalidad`         | object        | object     | **Categórica Nominal** | Causa de mortalidad (siempre "Suicidios") |
| `TipoPoblacionObjetivo`   | object        | category   | **Categórica Nominal** | Tipo de población analizada               |
| `NumeroPoblacionObjetivo` | object        | int64      | **Numérica (entera)**  | Población del municipio                   |
| `NumeroCasos`             | int64         | int64      | **Numérica (entera)**  | **Variable objetivo: casos de suicidio**  |

## 2.1 Interpretación de los Tipos de Datos Originales

Durante la ejecución del código, se imprimió la siguiente salida:

=== TIPOS DE DATOS ORIGINALES ===
NombreMunicipio            object
CodigoMunicipio             int64
Ubicación                  object
NombreRegion               object
CodigoRegion                int64
Anio                        int64
CausaMortalidad            object
TipoPoblacionObjetivo      object
NumeroPoblacionObjetivo    object
NumeroCasos                 int64
dtype: object

**Interpretación:**

Las columnas con tipo object representan texto o cadenas (por ejemplo: NombreMunicipio, Ubicación, NombreRegion, etc.).

Las columnas con tipo int64 son números enteros, útiles para cálculos y análisis estadísticos (por ejemplo: Anio, CodigoMunicipio, NumeroCasos).

La columna NumeroPoblacionObjetivo aparece como texto (object) porque contiene comas en los números, lo que impide reconocerla como número hasta limpiarla.

🧹**Solución aplicada:**

Para corregirlo y convertir esa columna a tipo numérico, se utilizó:

df['NumeroPoblacionObjetivo'] = df['NumeroPoblacionObjetivo'].str.replace(',', '').astype(int)


Esto elimina las comas y permite realizar operaciones matemáticas correctamente.

## 3. Transformaciones Aplicadas


En resumen:
👉 **Inserta la nueva sección justo entre** `## 2. Clasificación de Columnas por Tipo` **y** `## 3. Transformaciones Aplicadas`.


**A. Conversión de Variables Categóricas:**

```python
df['NombreRegion'] = df['NombreRegion'].astype('category')
df['TipoPoblacionObjetivo'] = df['TipoPoblacionObjetivo'].astype('category')
```

_Justificación:_ Optimización de memoria y mejora en rendimiento para operaciones de agrupación.

**B. Limpieza de Datos Numéricos:**

```python
df['NumeroPoblacionObjetivo'] = df['NumeroPoblacionObjetivo'].str.replace(',', '').astype(int)
```

_Justificación:_ Conversión de formato texto con comas a entero para cálculos matemáticos.

## 4. Resúmenes y Conclusiones

### Estadísticas Descriptivas Principales

**Variables Numéricas:**

- **Año:** Rango 2005-2024, distribución uniforme
- **Casos:** Promedio 3.17, mediana 1, máximo 246, desviación estándar 15.0
- **Población:** Promedio 49,355 habitantes, rango 2,629-2,616,335

**Distribución Regional:**

- Valle de Aburrá: 4,746 casos (59.8%)
- Oriente: 948 casos (11.9%)
- Suroeste: 573 casos (7.2%)
- Otras regiones: 1,649 casos (20.8%)

**Tendencia Temporal:**

- 2005-2014: Promedio 327 casos/año
- 2015-2019: Promedio 425 casos/año
- 2020-2024: Promedio 517 casos/año
- Pico histórico: 2023 con 586 casos

**Correlación Clave:**

- Población vs. Casos: r = 0.9973 (correlación casi perfecta)

### Conclusiones Principales

1. **Crisis concentrada:** El Valle de Aburrá representa el 60% de todos los casos
2. **Tendencia creciente:** Incremento sostenido del 79% en las últimas dos décadas
3. **Dualidad urbano-rural:** Grandes ciudades concentran casos absolutos, municipios pequeños muestran tasas desproporcionadas
4. **Medellín como epicentro:** 40.3% de todos los casos del departamento

## 5. Preguntas Relevantes sobre Problemas Reales

### 1. ¿Se puede identificar qué regiones de Antioquia requieren intervención prioritaria en salud mental?

**Respuesta:** ✅ **SÍ**  
**Justificación:** El dataset contiene `NombreRegion` y `NumeroCasos`, permitiendo calcular totales y tasas por región. Los datos muestran claramente que Valle de Aburrá requiere atención inmediata.

### 2. ¿Es posible predecir la tendencia de casos de suicidio para los próximos años?

**Respuesta:** ⚠️ **PARCIALMENTE**  
**Justificación:** Con 20 años de datos temporales (`Anio` y `NumeroCasos`) se pueden identificar tendencias históricas, pero la predicción requiere modelos estadísticos avanzados y variables adicionales (factores socioeconómicos, eventos externos).

### 3. ¿Se pueden identificar municipios pequeños con tasas de suicidio desproporcionadamente altas?

**Respuesta:** ✅ **SÍ**  
**Justificación:** Combinando `NumeroPoblacionObjetivo`, `NumeroCasos` y `NombreMunicipio` se pueden calcular tasas por 100,000 habitantes y identificar municipios con poblaciones menores a 10,000 habitantes pero tasas superiores al promedio nacional.

### 4. ¿Se puede determinar si existe correlación entre el tamaño poblacional y el número absoluto de casos?

**Respuesta:** ✅ **SÍ**  
**Justificación:** Las variables `NumeroPoblacionObjetivo` y `NumeroCasos` permiten calcular correlaciones. El análisis muestra r=0.9973, indicando relación casi perfecta entre tamaño poblacional y casos absolutos.

### 5. ¿Es posible diseñar un sistema de alerta temprana basado en patrones geográficos y temporales?

**Respuesta:** ⚠️ **PARCIALMENTE**  
**Justificación:** El dataset proporciona dimensiones geográficas (`NombreMunicipio`, `NombreRegion`) y temporales (`Anio`) suficientes para identificar patrones históricos, pero un sistema de alerta efectivo requeriría datos en tiempo real y variables predictivas adicionales (indicadores socioeconómicos, eventos estacionales, etc.).

---

**Archivos del proyecto, de donde fue extraída y analizada la información:**

- `main.py`: Script de análisis de datos.
- `suicidios-en-antioquia.csv`: Dataset fuente.
- `README.md`: Informe de análisis.

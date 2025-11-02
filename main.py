import pandas as pd

def main():
    print("=== ANÁLISIS DE SUICIDIOS EN ANTIOQUIA ===\n")
    
    # 1. Cargar el dataset
    print("Cargando dataset...")
    df = pd.read_csv('suicidios-en-antioquia.csv')
    
    # 2. Exploración inicial básica
    print("=== FORMA DEL DATASET ===")
    print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
    
    print("\n=== PRIMERAS 5 FILAS ===")
    print(df.head())
    
    print("\n=== TIPOS DE DATOS ACTUALES ===")
    print(df.dtypes)
    
    print("\n=== INFORMACIÓN GENERAL ===")
    print(df.info())
        # 3. LIMPIEZA Y TRANSFORMACIÓN (según documento permitido)
    print("\n" + "="*50)
    print("TRANSFORMACIÓN DE VARIABLES")
    print("="*50)
    
    # A. Convertir NumeroPoblacionObjetivo a numérico (quitando comas)
    print("Convirtiendo NumeroPoblacionObjetivo a numérico...")
    df['NumeroPoblacionObjetivo'] = df['NumeroPoblacionObjetivo'].str.replace(',', '').astype(int)
    
    # B. Convertir variables categóricas
    print("Convirtiendo variables categóricas...")
    df['NombreRegion'] = df['NombreRegion'].astype('category')
    df['CausaMortalidad'] = df['CausaMortalidad'].astype('category')
    df['TipoPoblacionObjetivo'] = df['TipoPoblacionObjetivo'].astype('category')
    
    # C. Verificar cambios
    print("\n=== TIPOS DE DATOS DESPUÉS DE TRANSFORMACIONES ===")
    print(df.dtypes)
    
    # D. Resumen estadístico de variables numéricas
    print("\n=== RESUMEN ESTADÍSTICO (NUMÉRICAS) ===")
    print(df.describe())

        # 3. CLASIFICACIÓN OFICIAL DE VARIABLES (según documento)
    print("\n" + "="*60)
    print("CLASIFICACIÓN DE VARIABLES SEGÚN DOCUMENTO")
    print("="*60)
    
    # Variables Numéricas (para cálculos)
    print(" VARIABLES NUMÉRICAS:")
    print("- CodigoMunicipio (int64)")
    print("- CodigoRegion (int64)") 
    print("- Anio (int64)")
    print("- NumeroCasos (int64)")
    
    # Variables Categóricas (para agrupar y contar)
    print("\n VARIABLES CATEGÓRICAS:")
    print("- NombreRegion (object → ideal para category)")
    print("- CausaMortalidad (object → ideal para category)")
    print("- TipoPoblacionObjetivo (object → ideal para category)")
    
    # Variables de Texto (para manipulación)
    print("\n VARIABLES DE TEXTO:")
    print("- NombreMunicipio (object)")
    print("- Ubicación (object)")
    
    # 4. RESUMENES BÁSICOS PERMITIDOS
    print("\n" + "="*60)
    print("RESUMENES ESTADÍSTICOS BÁSICOS")
    print("="*60)
    
    print("\n=== RESUMEN NUMÉRICO ===")
    print(df[['CodigoMunicipio', 'CodigoRegion', 'Anio', 'NumeroCasos']].describe())
    
    print("\n=== DISTRIBUCIÓN POR REGIÓN ===")
    print(df['NombreRegion'].value_counts())
    
    print("\n=== DISTRIBUCIÓN POR AÑO ===")
    print(df['Anio'].value_counts().sort_index())

        # 5. CONVERSIÓN A CATEGÓRICAS (según documento permitido)
    print("\n" + "="*50)
    print("CONVERSIÓN A VARIABLES CATEGÓRICAS")
    print("="*50)
    
    # Convertir a category como muestra el documento
    df['NombreRegion'] = df['NombreRegion'].astype('category')
    df['CausaMortalidad'] = df['CausaMortalidad'].astype('category')
    df['TipoPoblacionObjetivo'] = df['TipoPoblacionObjetivo'].astype('category')
    
    print(" Variables convertidas a categóricas")
    print(f"Tipos actualizados:\n{df[['NombreRegion', 'CausaMortalidad', 'TipoPoblacionObjetivo']].dtypes}")
    
    # 6. PRIMERAS RESPUESTAS A TUS PREGUNTAS
    print("\n" + "="*50)
    print("RESPUESTAS INICIALES A TUS PREGUNTAS")
    print("="*50)
    
    # Pregunta 1: ¿En qué años hubieron más suicidios?
    print("\n 1. TOTAL DE SUICIDIOS POR AÑO:")
    suicidios_por_anio = df.groupby('Anio')['NumeroCasos'].sum()
    print(suicidios_por_anio)
    
    # Pregunta 2: ¿Cuáles regiones tienen más suicidios?
    print("\n  2. TOTAL DE SUICIDIOS POR REGIÓN:")
    suicidios_por_region = df.groupby('NombreRegion')['NumeroCasos'].sum().sort_values(ascending=False)
    print(suicidios_por_region)

        # 7. ANÁLISIS DETALLADO DE REGIONES MÁS AFECTADAS
    print("\n" + "="*50)
    print("ANÁLISIS DETALLADO: REGIONES MÁS AFECTADAS")
    print("="*50)
    
    # Filtrar solo las dos regiones más afectadas (como muestra el documento)
    regiones_criticas = ['VALLE DE ABURRA', 'ORIENTE']
    df_regiones_criticas = df[df['NombreRegion'].isin(regiones_criticas)]
    
    print(" SUICIDIOS EN REGIONES CRÍTICAS POR AÑO:")
    suicidios_regiones_anio = df_regiones_criticas.groupby(['NombreRegion', 'Anio'])['NumeroCasos'].sum()
    print(suicidios_regiones_anio.head(10))  # Mostramos primeros 10 resultados
    
    # 8. IDENTIFICAR MUNICIPIOS MÁS AFECTADOS
    print("\n TOP 10 MUNICIPIOS CON MÁS CASOS:")
    top_municipios = df.groupby('NombreMunicipio')['NumeroCasos'].sum().sort_values(ascending=False).head(10)
    print(top_municipios)
    
        # 9. IDENTIFICAR PUNTOS CRÍTICOS ESPECÍFICOS
    print("\n" + "="*50)
    print("IDENTIFICACIÓN DE PUNTOS CRÍTICOS")
    print("="*50)
    
    # A. Municipio con MÁS casos en un solo año
    print(" MUNICIPIO CON MÁS CASOS EN UN AÑO:")
    max_casos = df['NumeroCasos'].max()
    municipio_max = df[df['NumeroCasos'] == max_casos][['NombreMunicipio', 'Anio', 'NumeroCasos']]
    print(municipio_max)
    
    # B. Año con MÁS casos totales
    print("\n AÑO CON MÁS SUICIDIOS TOTALES:")
    anio_max = df.groupby('Anio')['NumeroCasos'].sum().idxmax()
    total_anio_max = df.groupby('Anio')['NumeroCasos'].sum().max()
    print(f"Año: {anio_max}, Total casos: {total_anio_max}")
    
    # C. Top 5 municipios con más casos acumulados
    print("\n TOP 5 MUNICIPIOS (ACUMULADO TODOS LOS AÑOS):")
    top5_municipios = df.groupby('NombreMunicipio')['NumeroCasos'].sum().sort_values(ascending=False).head(5)
    print(top5_municipios)

        # 10. RESUMEN EJECUTIVO FINAL
    print("\n" + "="*60)
    print(" RESUMEN EJECUTIVO - SUICIDIOS EN ANTIOQUIA")
    print("="*60)
    
    # Hallazgos principales
    total_suicidios = df['NumeroCasos'].sum()
    años_analizados = df['Anio'].nunique()
    municipios_analizados = df['NombreMunicipio'].nunique()
    
    print(f" TOTAL SUICIDIOS REGISTRADOS: {total_suicidios:,}")
    print(f" PERIODO ANALIZADO: {años_analizados} años ({df['Anio'].min()} - {df['Anio'].max()})")
    print(f"  MUNICIPIOS ANALIZADOS: {municipios_analizados}")
    print(f" AÑO MÁS CRÍTICO: {anio_max} ({total_anio_max} casos)")
    print(f" REGIONES MÁS AFECTADAS: VALLE DE ABURRA y ORIENTE")
    
    # Municipio con máximo casos
    print(f"MUNICIPIO MÁS AFECTADO EN UN AÑO: {municipio_max['NombreMunicipio'].values[0]}")
    print(f"   - Año: {municipio_max['Anio'].values[0]}")
    print(f"   - Casos: {municipio_max['NumeroCasos'].values[0]}")
    
    print("\n" + "="*60)
    print(" ANÁLISIS COMPLETADO")
    print("="*60)
if __name__ == "__main__":
    main()
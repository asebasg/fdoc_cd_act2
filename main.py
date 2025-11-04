import pandas as pd

def main():
    print("="*60)
    print("ANÁLISIS DE SUICIDIOS EN ANTIOQUIA (2005-2024)")
    print("="*60)
    
    # 1. CARGAR DATOS
    df = pd.read_csv('suicidios-en-antioquia.csv')
    
    # 2. INFORMACIÓN BÁSICA
    print(f"\nLas dimensiones del DataFrame son: {df.shape[0]} filas x {df.shape[1]} columnas")
    
    print("\n=== TIPOS DE DATOS ORIGINALES ===")
    print(df.dtypes)
    
    # 3. TRANSFORMACIONES (solo las permitidas)
    print("\n=== APLICANDO TRANSFORMACIONES ===")
    
    # Limpiar y convertir NumeroPoblacionObjetivo
    df['NumeroPoblacionObjetivo'] = df['NumeroPoblacionObjetivo'].str.replace(',', '').astype(int)
    
    # Convertir variables categóricas
    df['NombreRegion'] = df['NombreRegion'].astype('category')
    df['TipoPoblacionObjetivo'] = df['TipoPoblacionObjetivo'].astype('category')
    
    print("✅ Las transformaciones han sido completadas exitosamente.")
    
    # 4. RESUMEN DE VARIABLES NUMÉRICAS
    print("\n=== RESUMEN DE VARIABLES NUMÉRICAS ===")
    print(df[['Anio', 'NumeroCasos', 'NumeroPoblacionObjetivo']].describe())
    
    # 5. RESPONDER LAS 5 PREGUNTAS
    print("\n" + "="*60)
    print("RESPUESTAS A PREGUNTAS CLAVE")
    print("-"*60)
    
    # Pregunta 1: Región con mayor necesidad de atención
    print("\n1️⃣  ¿Qué región requiere mayor atención?")
    casos_region = df.groupby('NombreRegion', observed=True)['NumeroCasos'].sum().sort_values(ascending=False)
    print(casos_region)
    
    # Pregunta 2: Tendencia temporal
    print("\n2️⃣  Tendencia de casos por año:")
    casos_anio = df.groupby('Anio')['NumeroCasos'].sum()
    print(casos_anio)
    print(f"Año con más casos: {casos_anio.idxmax()} ({casos_anio.max()} casos)")
    
    # Pregunta 3: Top 10 municipios
    print("\n3️⃣  Top 10 municipios más afectados:")
    top10 = df.groupby('NombreMunicipio')['NumeroCasos'].sum().sort_values(ascending=False).head(10)
    print(top10)
    
    # Pregunta 4: Análisis de municipios pequeños (esto requiere calcular tasas)
    print("\n4️⃣  Municipios pequeños con altas tasas:")
    # Agregar por municipio
    df_municipios = df.groupby('NombreMunicipio').agg({
        'NumeroCasos': 'sum',
        'NumeroPoblacionObjetivo': 'mean'  # Promedio de población
    }).reset_index()
    
    # Calcular tasa por 100,000 habitantes
    df_municipios['Tasa'] = (df_municipios['NumeroCasos'] / df_municipios['NumeroPoblacionObjetivo']) * 100000
    
    # Filtrar municipios pequeños (< 10,000 hab)
    municipios_pequeños = df_municipios[df_municipios['NumeroPoblacionObjetivo'] < 10000]
    print(municipios_pequeños.nlargest(5, 'Tasa')[['NombreMunicipio', 'Tasa']])
    
    # Pregunta 5: Correlación población-casos
    print("\n5️⃣  Correlación entre población y casos:")
    correlacion = df_municipios['NumeroPoblacionObjetivo'].corr(df_municipios['NumeroCasos'])
    print(f"   Coeficiente de correlación: {correlacion:.4f}")
    
    print("\nAnálisis completado.")

if __name__ == "__main__":
    main()
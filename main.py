import pandas as pd

def main():
    print("=" * 70)
    print("📊 ANÁLISIS DE SUICIDIOS EN ANTIOQUIA (2005–2024)")
    print("=" * 70)

    # 1️⃣ CARGAR DATOS
    print("\n🔹 Cargando los datos del archivo CSV...")
    df = pd.read_csv('suicidios-en-antioquia.csv')
    print(f"✅ Archivo cargado con éxito. Contiene {df.shape[0]} filas y {df.shape[1]} columnas.")

    # 2️⃣ INFORMACIÓN BÁSICA
    print("\n🔹 Mostrando información general del DataFrame:")
    print(f"\nLas dimensiones del DataFrame son: {df.shape[0]} filas x {df.shape[1]} columnas")
    print("\n=== TIPOS DE DATOS ORIGINALES ===")
    print(df.dtypes)

    # 3️⃣ TRANSFORMACIONES
    print("\n🔹 Iniciando proceso de limpieza y transformación de datos...")

    # Limpiar y convertir NumeroPoblacionObjetivo
    print("   - Limpiando la columna 'NumeroPoblacionObjetivo' (quitando comas y convirtiendo a número)...")
    df['NumeroPoblacionObjetivo'] = df['NumeroPoblacionObjetivo'].str.replace(',', '').astype(int)

    # Convertir variables categóricas
    print("   - Convirtiendo columnas categóricas ('NombreRegion', 'TipoPoblacionObjetivo')...")
    df['NombreRegion'] = df['NombreRegion'].astype('category')
    df['TipoPoblacionObjetivo'] = df['TipoPoblacionObjetivo'].astype('category')

    print("✅ Transformaciones completadas correctamente.")

    # 4️⃣ RESUMEN DE VARIABLES NUMÉRICAS
    print("\n🔹 Mostrando resumen estadístico de las variables numéricas:")
    print(df[['Anio', 'NumeroCasos', 'NumeroPoblacionObjetivo']].describe())

    # 5️⃣ RESPUESTAS A PREGUNTAS CLAVE
    print("\n" + "=" * 70)
    print("🔍 RESPUESTAS A PREGUNTAS CLAVE")
    print("-" * 70)

    # Pregunta 1: Región con mayor necesidad de atención
    print("\n1️⃣  ¿Qué región requiere mayor atención?")
    casos_region = df.groupby('NombreRegion', observed=True)['NumeroCasos'].sum().sort_values(ascending=False)
    print(casos_region)
    print(f"👉 La región con más casos es: {casos_region.idxmax()} con {casos_region.max()} casos en total.")

    # Pregunta 2: Tendencia temporal
    print("\n2️⃣  Analizando la tendencia de casos por año...")
    casos_anio = df.groupby('Anio')['NumeroCasos'].sum()
    print(casos_anio)
    print(f"📈 El año con más casos fue {casos_anio.idxmax()} con un total de {casos_anio.max()} casos reportados.")

    # Pregunta 3: Top 10 municipios
    print("\n3️⃣  Mostrando los 10 municipios más afectados por suicidios:")
    top10 = df.groupby('NombreMunicipio')['NumeroCasos'].sum().sort_values(ascending=False).head(10)
    print(top10)

    # Pregunta 4: Municipios pequeños con altas tasas
    print("\n4️⃣  Identificando municipios pequeños con tasas altas de suicidio...")
    df_municipios = df.groupby('NombreMunicipio').agg({
        'NumeroCasos': 'sum',
        'NumeroPoblacionObjetivo': 'mean'
    }).reset_index()

    # Calcular tasa por 100,000 habitantes
    df_municipios['Tasa'] = (df_municipios['NumeroCasos'] / df_municipios['NumeroPoblacionObjetivo']) * 100000
    municipios_pequeños = df_municipios[df_municipios['NumeroPoblacionObjetivo'] < 10000]

    print("📊 Municipios pequeños con las tasas más altas de suicidio:")
    print(municipios_pequeños.nlargest(5, 'Tasa')[['NombreMunicipio', 'Tasa']])

    # Pregunta 5: Correlación población-casos
    print("\n5️⃣  Calculando la correlación entre población y número de casos...")
    correlacion = df_municipios['NumeroPoblacionObjetivo'].corr(df_municipios['NumeroCasos'])
    print(f"🔗 Coeficiente de correlación: {correlacion:.4f}")
    if correlacion > 0.5:
        print("➡️ Existe una fuerte correlación positiva: a mayor población, más casos.")
    elif correlacion < -0.5:
        print("⬇️ Existe una correlación negativa: los municipios con más población tienden a tener menos casos.")
    else:
        print("⚖️ La correlación es baja o casi nula entre población y casos.")

    print("\n✅ Análisis finalizado correctamente.")
    print("=" * 70)
    print("🧠 Fin del análisis de datos. Gracias por usar este programa.")
    print("=" * 70)

if __name__ == "__main__":
    main()

import pandas as pd
import os

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"
    """
    # Ruta del archivo de entrada y salida
    input_path = "files/input/solicitudes_de_credito.csv"
    output_path = "files/output/solicitudes_de_credito.csv"

    # Verificar si la carpeta de salida existe, si no, crearla
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Cargar los datos del archivo CSV
    try:
        df = pd.read_csv(input_path, sep=";")
    except FileNotFoundError:
        print(f"El archivo de entrada no existe en la ruta especificada: {input_path}")
        return

    # Eliminar registros duplicados
    df = df.drop_duplicates()

    # Eliminar filas con valores nulos en columnas críticas
    columnas_criticas = [
        'sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 
        'estrato', 'comuna_ciudadano', 'fecha_de_beneficio', 
        'monto_del_credito', 'línea_credito'
    ]
    df = df.dropna(subset=columnas_criticas)

    # Normalizar columnas de texto
    df['sexo'] = df['sexo'].str.lower().str.strip()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower().str.strip()
    df['idea_negocio'] = df['idea_negocio'].str.lower().str.strip()
    df['barrio'] = df['barrio'].str.lower().str.strip()
    df['línea_credito'] = df['línea_credito'].str.lower().str.strip()

    # Convertir la columna 'fecha_de_beneficio' a formato datetime
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], errors='coerce')

    # Filtrar filas con fechas inválidas
    df = df.dropna(subset=['fecha_de_beneficio'])

    # Asegurar que 'estrato' sea numérico
    df['estrato'] = pd.to_numeric(df['estrato'], errors='coerce')

    # Eliminar filas con valores nulos en 'estrato' después de la conversión
    df = df.dropna(subset=['estrato'])

    # Normalizar la columna 'monto_del_credito' eliminando caracteres especiales y convirtiendo a numérico
    df['monto_del_credito'] = (
        df['monto_del_credito']
        .str.replace(r'[^\d]', '', regex=True)  # Eliminar caracteres no numéricos
        .astype(float)
    )

    # Guardar el archivo limpio en la ubicación indicada
    df.to_csv(output_path, index=False, sep=";")
    print(f"Archivo limpio guardado en: {output_path}")

pregunta_01()

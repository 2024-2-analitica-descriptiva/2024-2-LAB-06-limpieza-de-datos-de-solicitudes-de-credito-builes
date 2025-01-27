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
    
    # Ruta de salida
    output_path = "../files/output/solicitudes_de_credito.csv"
    
    # Verificar si la carpeta de salida existe, si no, crearla
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Cargar los datos del archivo CSV
    df = pd.read_csv("../files/input/solicitudes_de_credito.csv", sep=";")
    
    # Eliminar registros duplicados
    df = df.drop_duplicates()
    
    # Manejo de datos faltantes
    # Por ejemplo, podemos eliminar filas con datos faltantes en columnas críticas
    df = df.dropna(subset=['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'estrato', 'comuna_ciudadano', 'fecha_de_beneficio', 'monto_del_credito', 'línea_credito'])
    
    # Corregir los valores de texto con errores o inconsistencias (por ejemplo, capitalización de 'sexo')
    df['sexo'] = df['sexo'].str.lower()
    
    # Normalizar fechas (convertir a formato estándar)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], errors='coerce')
    
    # Corregir estrato, por ejemplo, asegurarse de que sean valores numéricos
    df['estrato'] = pd.to_numeric(df['estrato'], errors='coerce')
    
    # Rellenar o eliminar valores nulos después de la conversión
    df['estrato'] = df['estrato'].fillna(df['estrato'].median())
    
    # Guardar el archivo limpio en la ubicación indicada
    df.to_csv(output_path, index=False, sep=";")
    

pregunta_01()
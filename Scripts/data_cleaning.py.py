import pandas as pd

# Cargar datos
data = pd.read_csv('raw_data.csv', parse_dates=True, index_col='Date')

# Inspeccionar datos
print("Información inicial de los datos:")
print(data.info())

# Eliminar duplicados (si los hay)
data_cleaned = data.drop_duplicates()
print(f"Duplicados eliminados. Filas originales: {len(data)}, Filas después: {len(data_cleaned)}")

# Manejar valores nulos (si los hay)
if data_cleaned.isnull().values.any():
    data_cleaned = data_cleaned.fillna(method='ffill')
    print("Valores nulos encontrados y tratados.")

# Filtrar por fechas
data_cleaned = data_cleaned[(data_cleaned.index >= '2019-06-01') & (data_cleaned.index <= '2022-6-30')]

# Inspeccionar datos después de la limpieza
print("Información de los datos después de la limpieza:")
print(data_cleaned.info())

# Guardar el DataFrame limpio
data_cleaned.to_csv('cleaned_data.csv')
print("Data cleaning completed and saved to 'cleaned_data.csv'")
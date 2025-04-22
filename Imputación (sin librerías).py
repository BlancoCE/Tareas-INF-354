#Rellenar valores faltantes en los datos.
#Ejemplo de imputación con la media:
def impute_missing(values):
    # Calcular media ignorando valores None
    valid_values = [v for v in values if v is not None]
    mean = sum(valid_values) / len(valid_values) if valid_values else 0
    
    # Reemplazar None con la media
    return [v if v is not None else mean for v in values]

datos = [1, 2, None, 4, 5, None, 7]
imputed = impute_missing(datos)
print(imputed)  # [1, 2, 3.8, 4, 5, 3.8, 7]

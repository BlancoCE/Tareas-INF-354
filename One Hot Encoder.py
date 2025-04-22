#Convierte variables categóricas en un conjunto de variables binarias (0 o 1), creando una columna por cada categoría.
#Ejemplo sin librerías:
def one_hot_encoder(categories):
    unique_cats = list(set(categories))
    encoded = []
    for cat in categories:
        vector = [1 if cat == uc else 0 for uc in unique_cats]
        encoded.append(vector)
    return encoded

colores = ['rojo', 'azul', 'verde', 'azul', 'rojo']
encoded = one_hot_encoder(colores)
print(encoded)
# [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]

def label_encoder(categories):
    unique_cats = list(set(categories))
    mapping = {cat: idx for idx, cat in enumerate(unique_cats)}
    return [mapping[cat] for cat in categories]

colores = ['rojo', 'azul', 'verde', 'azul', 'rojo']
encoded = label_encoder(colores)
print(encoded)  # [1, 0, 2, 0, 1] (los números pueden variar)

"""
Label Encoding Manual para el dataset Iris
"""

def manual_label_encoder(labels):
    unique_labels = sorted(list(set(labels)))
    label_to_code = {label: idx for idx, label in enumerate(unique_labels)}
    encoded_labels = [label_to_code[label] for label in labels]
    return encoded_labels, label_to_code

def run_label_encoding(y):
    print("\n=== Label Encoding Manual ===")
    y_encoded, mapping = manual_label_encoder(y)
    print("Original (primeras 10 muestras):", y[:10])
    print("Codificado (primeras 10 muestras):", y_encoded[:10])
    print("Mapeo de clases:", mapping)
    
    return y_encoded

if __name__ == "__main__":
    from sklearn.datasets import load_iris
    iris = load_iris()
    run_label_encoding(iris.target)
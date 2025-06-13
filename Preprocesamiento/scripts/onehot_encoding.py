"""
One-Hot Encoding Manual para el dataset Iris
"""
import numpy as np

def manual_one_hot_encoder(labels, num_classes=None):
    if num_classes is None:
        num_classes = len(set(labels))
    
    one_hot = []
    for label in labels:
        vector = [0] * num_classes
        vector[label] = 1
        one_hot.append(vector)
    
    return np.array(one_hot)

def run_onehot_encoding(encoded_labels):
    print("\n=== One-Hot Encoding Manual ===")
    one_hot = manual_one_hot_encoder(encoded_labels, num_classes=3)
    print("One-Hot Encoding de las primeras 5 muestras:")
    print(one_hot[:5])
    return one_hot

if __name__ == "__main__":
    from sklearn.datasets import load_iris
    iris = load_iris()
    y_encoded = __import__("label_encoding").run_label_encoding(iris.target)
    run_onehot_encoding(y_encoded)
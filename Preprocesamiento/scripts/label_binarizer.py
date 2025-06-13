"""
Label Binarizer Manual para el dataset Iris
"""

def manual_label_binarizer(labels, positive_class=0):
    return [1 if label == positive_class else 0 for label in labels]

def run_label_binarizer(y_encoded):
    print("\n=== Label Binarizer Manual ===")
    y_binary = manual_label_binarizer(y_encoded, positive_class=0)
    print("Ejemplo (setosa vs resto):")
    print("Original:", y_encoded[:10])
    print("Binario:", y_binary[:10])
    return y_binary

if __name__ == "__main__":
    from sklearn.datasets import load_iris
    iris = load_iris()
    y_encoded = __import__("label_encoding").run_label_encoding(iris.target)
    run_label_binarizer(y_encoded)
"""
Script principal para preprocesamiento del dataset Iris
"""
from sklearn.datasets import load_iris
from scripts import (
    label_encoding,
    onehot_encoding,
    label_binarizer,
    imputacion_manual,
    pipeline_sklearn,
    pipeline_manual
)

def main():
    print("=== INICIO DEL PREPROCESAMIENTO ===")
    
    # Cargar el dataset una sola vez
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # Ejecutar cada script pasando los datos
    y_encoded = label_encoding.run_label_encoding(y)
    onehot = onehot_encoding.run_onehot_encoding(y_encoded)
    label_binarizer.run_label_binarizer(y_encoded)
    imputacion_manual.run_imputation(X.copy())
    pipeline_sklearn.run_sklearn_pipeline(X.copy(), y)
    pipeline_manual.run_manual_pipeline(X.copy(), y)
    
    print("\n=== PREPROCESAMIENTO COMPLETADO ===")

if __name__ == "__main__":
    main()
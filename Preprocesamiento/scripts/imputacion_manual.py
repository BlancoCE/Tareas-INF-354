"""
Imputación Manual para el dataset Iris
"""
import numpy as np

def manual_imputer(data):
    imputed_data = data.copy()
    for col in range(data.shape[1]):
        col_values = data[:, col]
        mean_val = np.nanmean(col_values)
        nan_indices = np.where(np.isnan(col_values))[0]
        imputed_data[nan_indices, col] = mean_val
    return imputed_data

def run_imputation(X):
    print("\n=== Imputación Manual de Valores Faltantes ===")
    # Crear datos faltantes artificiales
    np.random.seed(42)
    X_missing = X.copy()
    mask = np.random.rand(*X.shape) < 0.05
    X_missing[mask] = np.nan
    
    print("Valores faltantes por característica (antes):", np.isnan(X_missing).sum(axis=0))
    X_imputed = manual_imputer(X_missing)
    print("Valores faltantes por característica (después):", np.isnan(X_imputed).sum(axis=0))
    return X_imputed

if __name__ == "__main__":
    from sklearn.datasets import load_iris
    iris = load_iris()
    run_imputation(iris.data)
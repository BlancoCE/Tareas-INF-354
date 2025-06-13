"""
Pipeline Manual para el dataset Iris
"""
import numpy as np

class ManualPipeline:
    def __init__(self):
        self.num_means = None
        self.num_stds = None
        
    def fit(self, X):
        # Calcular media y std para normalización
        self.num_means = np.nanmean(X, axis=0)
        self.num_stds = np.nanstd(X, axis=0)
        return self
    
    def transform(self, X):
        # 1. Imputar valores faltantes
        X_imputed = X.copy()
        for col in range(X.shape[1]):
            X_imputed[np.isnan(X_imputed[:, col]), col] = self.num_means[col]
        
        # 2. Estandarizar
        X_normalized = (X_imputed - self.num_means) / self.num_stds
        return X_normalized
    
    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

def run_manual_pipeline(X, y=None):
    print("\n=== Pipeline Manual ===")
    
    # Crear datos con valores faltantes
    np.random.seed(42)
    X_missing = X.copy()
    mask = np.random.rand(*X.shape) < 0.05
    X_missing[mask] = np.nan
    
    # Aplicar pipeline manual
    pipeline = ManualPipeline()
    X_processed = pipeline.fit_transform(X_missing)
    
    print("Datos originales (primeras 3 filas):")
    print(X[:3])
    print("\nDatos con valores faltantes (primeras 3 filas):")
    print(X_missing[:3])
    print("\nDatos procesados (primeras 3 filas):")
    print(X_processed[:3])

if __name__ == "__main__":
    from sklearn.datasets import load_iris
    iris = load_iris()
    run_manual_pipeline(iris.data)
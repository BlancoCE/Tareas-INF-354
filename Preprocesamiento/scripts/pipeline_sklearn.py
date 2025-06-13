"""
Pipeline con Scikit-learn para el dataset Iris
"""
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

def run_sklearn_pipeline(X, y):
    print("\n=== Pipeline con Scikit-learn ===")
    
    # Pipeline simple con imputación, escalado y modelo
    pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler()),
        ('clf', LogisticRegression())
    ])
    
    # Entrenamiento (aquí usamos todos los datos solo como ejemplo)
    pipeline.fit(X, y)
    score = pipeline.score(X, y)
    
    print(f"Precisión del modelo: {score:.2f}")
    print("Pasos del pipeline:", pipeline.named_steps.keys())

if __name__ == "__main__":
    from sklearn.datasets import load_iris
    iris = load_iris()
    run_sklearn_pipeline(iris.data, iris.target)
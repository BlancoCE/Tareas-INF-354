#Un pipeline permite encadenar múltiples pasos de preprocesamiento y modelado en una secuencia ordenada.
#Ejemplo básico sin librerías:
class SimplePipeline:
    def __init__(self, steps):
        self.steps = steps
    
    def fit_transform(self, data):
        transformed = data
        for name, step in self.steps:
            transformed = step.fit_transform(transformed)
        return transformed

# Ejemplo de uso
pipeline = SimplePipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('encoder', SimpleOneHotEncoder())
])

datos_processed = pipeline.fit_transform(datos)

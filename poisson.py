import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import PoissonRegressor

# Diccionario con datos de registros nuevos y suscriptores
datos = {
    'registros_nuevos': [150, 70, 200, 90],
    'suscriptores': [7, 2, 9, 3]
}

# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(datos)

# Crear el modelo de regresion de Poisson
modelo_poisson = PoissonRegressor()

# Ajustar el modelo a los datos
X = df[['registros_nuevos']]
y = df['suscriptores']
modelo_poisson.fit(X, y)

# Predecir el num de suscriptores para un nuevo valor de registros nuevos
nuevos_registros = 250
prediccion_suscriptores = modelo_poisson.predict([[nuevos_registros]])
print(f"Num de suscriptores previsto para {nuevos_registros} registros nuevos: {prediccion_suscriptores[0]:.2f}")

# Visualizar
plt.scatter(df['registros_nuevos'], df['suscriptores'], label='Datos reales')
plt.plot(np.linspace(50, 250, 100), modelo_poisson.predict(np.linspace(50, 250, 100).reshape(-1, 1)), color='red', label='Prediccion (curva)')
plt.xlabel('Registros Nuevos')
plt.ylabel('Suscriptores')
plt.title('Relacion entre Registros Nuevos y Suscriptores')
plt.legend()
plt.show()
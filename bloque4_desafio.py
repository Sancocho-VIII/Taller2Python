import pandas as pd
import matplotlib.pyplot as plt
datos = {
'reactor': ['R1','R1','R1','R2','R2','R2','R3','R3'],
'turno': ['manana','tarde','noche','manana','tarde','noche','manana','tarde'],
'temperatura': [85, 92, 78, 95, 88, 91, 76, 83],
'eficiencia': [91.2, 87.5, 94.1, 83.3, 89.7, 85.0, 96.4, 92.8],
'incidentes': [0, 1, 0, 2, 0, 1, 0, 0]
}
df = pd.DataFrame(datos)
df['estado'] = df['temperatura'].apply(lambda t: 'critico' if t > 90 else 'normal')
print(df)
estado=df['estado'].value_counts()
print('-----CONTEO DE ESTADO-----')
print(estado)
plt.figure(figsize=(8, 4))
efprom_reactor = df.groupby('reactor')['eficiencia'].mean()
plt.bar(efprom_reactor.index, efprom_reactor.values, color = ['green', 'blue', 'orange'])
plt.title('Eficiencia promedio por reactor')
plt.xlabel('Reactor')
plt.ylabel('Eficiencia promedio (%)')
plt.tight_layout()
plt.show()

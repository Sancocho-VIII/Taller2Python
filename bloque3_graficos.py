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
plt.figure(figsize=(7, 4))
# plt.scatter(valores_eje_X, valores_eje_Y)
temp=df['temperatura']
ef=df['eficiencia']
# ESCRIBE TU CODIGO — usa df['temperatura'] y df['eficiencia']:
plt.scatter(temp.values, ef.values , color='coral', s=80)
plt.title('Temperatura vs Eficiencia')
plt.xlabel('Temperatura (C)')
plt.ylabel('Eficiencia (%)')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
# ESCRIBE TU CODIGO — usa plt.plot()
efmed = df['eficiencia']
plt.plot(efmed.index, efmed.values, marker='o', linewidth=2, color= 'peru')
plt.title('Eficiencia por medicion')
plt.xlabel('Numero de medicion')
plt.ylabel('Eficiencia (%)')
plt.tight_layout()
plt.show()
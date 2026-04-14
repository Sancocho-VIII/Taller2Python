import pandas as pd
datos = {
'reactor': ['R1','R1','R1','R2','R2','R2','R3','R3'],
'turno': ['manana','tarde','noche','manana','tarde','noche','manana','tarde'],
'temperatura': [85, 92, 78, 95, 88, 91, 76, 83],
'eficiencia': [91.2, 87.5, 94.1, 83.3, 89.7, 85.0, 96.4, 92.8],
'incidentes': [0, 1, 0, 2, 0, 1, 0, 0]
}
# pd.DataFrame() convierte el diccionario en tabla
df = pd.DataFrame(datos)
# Imprime solo la columna 'turno':
print(df['turno'])
print(df[['reactor', 'incidentes']])
# Filtro 1: filas donde el turno es exactamente 'manana'
# Para comparar texto usa == (doble igual)
manana = df[ df['turno']=="manana" ]
print('Turno manana:')
print(manana)
# Filtro 2: filas donde no hubo ningun incidente (incidentes == 0)
sin_incidentes = df[ df['incidentes']==0 ]
print('Sin incidentes:')
print(sin_incidentes)
# 1. Eficiencia PROMEDIO por turno (manana, tarde, noche):
# groupby 'turno', columna 'eficiencia', funcion .mean()
ef_turno = df.groupby('turno')['eficiencia'].mean()
print('Eficiencia promedio por turno:')
print(ef_turno)
# 2. Total de incidentes por reactor:
# groupby 'reactor', columna 'incidentes', funcion .sum()
inc_reactor = df.groupby('reactor')['incidentes'].sum()
print('Total incidentes por reactor:')
print(inc_reactor)






# Imprime las columnas 'reactor' e 'incidentes' juntas:

import pandas as pd

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
                      'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, 10, 9, 20, 14.5, 12, 8, 19], 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data)#, index=labels)
df.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#print(df)


#Punto 1 (Seleccione solo las columnas name y score.)
df_name = df.iloc[:,0]
df_score = df.score
#print(df_score)

#Punto 2 (Filtre las filas donde el número de intentos (attemps) sea mayor que 2.)
df_attM2 = df.loc[df.attempts > 2]
#print(df_attM2)

#Punto 3 (Filtre las filas donde el score se encuentre entre 15 y 20 (incluidos))
df_score15y20 = df.loc[(df['score'] >= 15) & (df.score <= 20)]
df_scoreb1520 = df.loc[df.score.between(15,20)]
#print(df_score15y20)
#print(df_scoreb1520)

#Punto 4 (Cambie el score en la fila 'd' a 11.5)
#df.score['d'] = 11.5
df.loc['d','score'] = 11.5
#print(df)

#Punto 5
#(Agregue una nueva fila con etiqueta 'k' al dataframe con un valor que usted desee para cada columna)
df.loc['k'] = ['Fernando', 20, 3, 'yes']
#print(df)

#Punto 6 (Borre la fila 'k' y entregue nuevamente el DataFrame original.)
df.drop(index='k',axis=0, inplace=True)
#print(df)

#Punto 7 (Ordene el DataFrame por nombre en orden ascendente.)
df.sort_values('name', ascending=True, inplace=True)
#print(df)

'''
#Punto 8 
(Reemplace los valores de la columna qualify que contiene los valores yes y no por los valores
booleanos True y False respectivamente.)'''
df['qualify'] = df['qualify'].map({'yes' : True, 'no' : False})
#print(df)
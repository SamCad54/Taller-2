#1
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dimension=np.array([100,40,30,10])
matriz= np.random.rand(*dimension)
#print(matriz)
#2
matriz_2=matriz[:,:,:,1].copy()
#print("la matriz copia es ", matriz_2)
#3
forma=matriz_2.shape
tamaño=matriz_2.size
dimension_2=matriz_2.ndim
tipo_datos=matriz_2.dtype
#print("la forma es: ",forma)
#print("el tamño  es: ",tamaño)
#print("la dimensión es: ",dimension)
#print("el tipo de datos es: ",tipo_datos)
#4
matriz_3=matriz_2[:,:,1]
matriz_3.shape
print(matriz_3)
def conversor(matriz_3):
    data_frame=pd.DataFrame(matriz_3)
    return data_frame
a=conversor(matriz_3)
#print(a)
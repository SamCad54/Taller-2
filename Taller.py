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
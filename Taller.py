#1
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dimension=np.array([100,40,30,10])
matriz= np.random.rand(*dimension)
#2
matriz_2=matriz[:,:,:,1].copy()
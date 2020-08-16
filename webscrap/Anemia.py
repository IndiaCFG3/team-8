import pandas as pd
import numpy as np

anemia = pd.read_csv("D:/Code for good/CSV/Anemia.csv")
anemia_ext = anemia.iloc[:,[1,2,3,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]]
anemia_fin = anemia_ext.replace(np.nan, -1)

import pandas as pd
import numpy as np

protein = pd.read_csv("D:/Code for good/CSV/Country dietary needs.csv")

protein_fin = protein[["country","Legumes_2016","Milk_2016","Processed meat_2016","Red meat_2016"]]	

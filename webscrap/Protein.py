import pandas as pd
import numpy as np
protein = pd.read_csv("../CSV Files/Country dietary needs.csv")
print(protein.keys())
print(protein["disagg.value"])
protein_fin = protein[protein["disagg.value"] == "National"][["country","Legumes_2016","Milk_2016","Processed meat_2016","Red meat_2016"]]
print(protein_fin.head())
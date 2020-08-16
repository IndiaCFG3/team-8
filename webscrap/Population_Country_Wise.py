import pandas as pd
import numpy as np

dataset = pd.read_csv("D:/Code for good/FAOSTAT.csv")

new_data = dataset[dataset["Unit"]=="tonnes"]
Extracted_data = new_data[["Area","Item Code","Year","Value"]][dataset["Item Code"]==1062][["Area","Year","Value"]]

population = pd.read_csv("D:/Code for good/FAOSTAT_Population.csv")

popu = population[population["Element"]=="Total Population - Both sexes"][["Area","Year","Value"]]
popu["Value"] = popu["Value"]*1000
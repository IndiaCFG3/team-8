import pandas as pd
import numpy as np

coun_code = pd.read_csv("D:/Code for good/CSV/Country_Code_Name.csv")
coun_code = coun_code.iloc[:,[0,1]]
coun_code = coun_code.drop_duplicates()


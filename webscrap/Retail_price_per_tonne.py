import pandas as pd
import numpy as np

prices = pd.read_csv("D:/Code for good/CSV/Retail_Prices.csv")
prices = prices[prices["Unit"]=="tonnes"][["Area","Year","Value"]]

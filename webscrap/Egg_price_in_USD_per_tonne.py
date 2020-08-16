import pandas as pd
import numpy as np

supply_prices = pd.read_csv("D:/Code for good/FAOSTAT_Supply_price.csv")

price1 = supply_prices[supply_prices["Months"]=="Annual value"]

price_USD = price1[price1["Unit"]=="USD"]

Final_price_list = price_USD[["Area","Year","Value"]]

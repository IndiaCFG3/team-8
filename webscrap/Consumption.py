import pandas as pd
import numpy as np

consumption = pd.read_csv("D:/Code for good/CSV/Consumption.csv")
consumption = consumption[["Country","Year","Value"]]

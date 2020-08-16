import pandas as pd
import numpy as np

stunting = pd.read_csv("D:/Code for good/CSV/Stunting - Trend.csv")
stunting.rename(columns = {'National':'Point Estimate','Unnamed: 14':'Lower Limit', 'Unnamed: 15':'Upper Limit', 
                              'Unnamed: 16':'Sample Size'}, inplace = True)

stunting2 = stunting[2:][["Countries and areas","Survey Years",'Point Estimate','Lower Limit','Upper Limit','Sample Size']]	

stunting2 = stunting2.replace(np.nan, -1)

wasting = pd.read_csv("D:/Code for good/CSV/Wasting - Trend.csv")

wasting.rename(columns = {'National':'Point Estimate','Unnamed: 14':'Lower Limit', 'Unnamed: 15':'Upper Limit', 
                              'Unnamed: 16':'Sample Size'}, inplace = True)

wasting2 = wasting[2:][["Countries and areas","Survey Years",'Point Estimate','Lower Limit','Upper Limit','Sample Size']]	

wasting2 = wasting2.replace(np.nan, -1)

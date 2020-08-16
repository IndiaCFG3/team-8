def supply(dataframe, country):
    data = dataframe[dataframe["Country"].str.contains("country")]
    print(data.head())
if __name__ == '__main__':
    supply()

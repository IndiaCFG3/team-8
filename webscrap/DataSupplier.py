from json import dumps

import pandas as pd


class DataSupplier:
    def __init__(self):
        dataset = pd.read_csv("../data.csv")
        new_data = dataset[dataset["Unit"] == "tonnes"]
        self.clean_data = new_data[["Area", "Item Code", "Year", "Value"]][dataset["Item Code"] == 1062][
            ["Area", "Year", "Value"]]

    def get_supply_data_by_country(self, country):
        country = country[0].capitalize() + country[1:]
        data = self.clean_data[self.clean_data["Area"].eq(country)]
        years = data["Year"].tolist()
        values = data["Value"].tolist()
        final_data = {
            "years": years,
            "values": values
        }
        return dumps(final_data)


if __name__ == '__main__':
    datasupplier = DataSupplier()
    print(datasupplier.get_supply_data_by_country("Afghanistan"))

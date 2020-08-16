from json import dumps

import pandas as pd


class DataSupplier:
    def __init__(self):
        dataset = pd.read_csv("/home/aayush/CFG/analysis/FAOSTAT_data_8-16-2020 (1).csv")
        new_data = dataset[dataset["Unit"] == "tonnes"]
        self.clean_data = new_data[["Area", "Item Code", "Year", "Value"]][dataset["Item Code"] == 1062][
            ["Area", "Year", "Value"]]

    def get_supply_data_by_country(self, country):
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

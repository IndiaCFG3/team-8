from json import dumps

import pandas as pd


def get_dataframe():
    dataset = pd.read_csv("/home/aayush/CFG/analysis/FAOSTAT_data_8-16-2020 (1).csv")

    new_data = dataset[dataset["Unit"] == "tonnes"]
    Extracted_data = new_data[["Area", "Item Code", "Year", "Value"]][dataset["Item Code"] == 1062][
        ["Area", "Year", "Value"]]
    # print(Extracted_data)
    return Extracted_data


def supply(dataframe, country):
    data = dataframe[dataframe["Area"].eq(country)]
    years = data["Year"].tolist()
    values = data["Value"].tolist()
    final_data = {
        "years": years,
        "values": values
    }
    print(dumps(final_data))


if __name__ == '__main__':
    all_data = get_dataframe()
    supply(all_data, "Afghanistan")

from json import dumps

import pandas as pd


class DataSupplier:
    def __init__(self):
        dataset = pd.read_csv("../data.csv")
        new_data = dataset[dataset["Unit"] == "tonnes"]
        self.clean_data = new_data[["Area", "Item Code", "Year", "Value"]][dataset["Item Code"] == 1062][
            ["Area", "Year", "Value"]]
        population = pd.read_csv("../CSV Files/FAOSTAT_Population.csv")
        popu = population[population["Element"] == "Total Population - Both sexes"][["Area", "Year", "Value"]]
        popu["Value"] = popu["Value"] * 1000
        self.population = popu
        protein = pd.read_csv("../CSV Files/Country dietary needs.csv")
        self.protein = protein[protein["disagg.value"] == "National"][
            ["country", "Legumes_2016", "Milk_2016", "Processed meat_2016", "Red meat_2016"]]
        supply_prices = pd.read_csv("../CSV Files/FAOSTAT_Supply_price.csv")
        price1 = supply_prices[supply_prices["Months"] == "Annual value"]
        price_USD = price1[price1["Unit"] == "USD"]
        self.prices = price_USD[["Area", "Year", "Value"]]

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

    def get_per_person_per_country(self, country):
        country = country[0].capitalize() + country[1:]
        supply = self.clean_data[self.clean_data["Area"].eq(country)][["Year", "Value"]]
        popu = self.population[self.population["Area"].eq(country)][["Year", "Value"]]
        years_supply = supply["Year"].tolist()
        years_popu = popu["Year"].tolist()
        years_total = list(set(years_supply) & set(years_popu))
        supply.set_index("Year", drop=True, inplace=True)
        popu.set_index("Year", drop=True, inplace=True)
        supply = supply.filter(years_total, axis=0)
        popu = popu.filter(years_total, axis=0)
        supply_per_popu = supply.div(popu)
        years = supply_per_popu.index.values.tolist()
        values = supply_per_popu["Value"].tolist()
        final_data = {
            "years": years,
            "values": values
        }
        return dumps(final_data)

    def protein_consumption_by_country(self, country):
        country = country[0].capitalize() + country[1:]
        prtn = self.protein[self.protein['country'] == country].to_dict('records')[0]
        return dumps(prtn)

    def egg_price_by_country(self, country):
        country = country[0].capitalize() + country[1:]
        data = self.prices[self.prices['Area'] == country]
        years = data["Year"].tolist()
        values = data["Value"].tolist()
        final_data = {
            "years": years,
            "values": values
        }
        return dumps(final_data)

    def population_by_country(self, country):
        country = country[0].capitalize() + country[1:]
        data = self.population[self.population['Area'] == country]
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
    print(datasupplier.get_per_person_per_country("Afghanistan"))
    print(datasupplier.protein_consumption_by_country("India"))
    print(datasupplier.egg_price_by_country("India"))
    print(datasupplier.population_by_country("Afghanistan"))
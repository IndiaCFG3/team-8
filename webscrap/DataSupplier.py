from json import dumps

import numpy as np
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

        stunting = pd.read_csv("../CSV Files/Stunting - Trend.csv")
        stunting.rename(
            columns={'National': 'Point Estimate', 'Unnamed: 14': 'Lower Limit', 'Unnamed: 15': 'Upper Limit',
                     'Unnamed: 16': 'Sample Size'}, inplace=True)
        stunting = stunting[2:][
            ["Countries and areas", "Survey Years", 'Point Estimate', 'Lower Limit', 'Upper Limit', 'Sample Size']]
        stunting = stunting.replace(np.nan, None)
        self.stunting = stunting

        wasting = pd.read_csv("../CSV Files/Wasting - Trend.csv")
        wasting.rename(
            columns={'National': 'Point Estimate', 'Unnamed: 14': 'Lower Limit', 'Unnamed: 15': 'Upper Limit',
                     'Unnamed: 16': 'Sample Size'}, inplace=True)
        wasting = wasting[2:][
            ["Countries and areas", "Survey Years", 'Point Estimate', 'Lower Limit', 'Upper Limit', 'Sample Size']]
        wasting = wasting.replace(np.nan, None)
        self.wasting = wasting

        retail_prices = pd.read_csv("../CSV Files/Retail_Prices.csv")
        retail_prices = retail_prices[retail_prices["Unit"] == "tonnes"][["Area", "Year", "Value"]]
        self.retail_prices = retail_prices

        consumption = pd.read_csv("../CSV Files/Consumption.csv")
        consumption = consumption[["Country", "Year", "Value"]]
        self.consumption = consumption

        anemia = pd.read_csv("../CSV Files/Anemia.csv")
        anemia = anemia.iloc[:, [1, 2, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]]
        anemia = anemia.replace(np.nan, None)
        self.anemia = anemia

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

    def stunting_by_country(self, country):
        country = country[0].capitalize() + country[1:]
        data = self.stunting[self.stunting['Countries and areas'] == country]
        years = data["Survey Years"].tolist()
        pt_estimate = data['Point Estimate'].tolist()
        lower_limit = data["Lower Limit"].tolist()
        upper_limit = data['Upper Limit'].tolist()
        sample_size = data['Sample Size'].tolist()

        final_data = {
            "years": years,
            "Point Estimate": pt_estimate,
            "Lower Limit": lower_limit,
            "Upper Limit": upper_limit,
            "Sample Size": sample_size,
        }
        return dumps(final_data)

    def wasting_by_country(self, country):
        country = country[0].capitalize() + country[1:]
        data = self.wasting[self.wasting['Countries and areas'] == country]
        years = data["Survey Years"].tolist()
        pt_estimate = data['Point Estimate'].tolist()

        final_data = {
            "years": years,
            "values": pt_estimate,
        }
        return dumps(final_data)

    def retail_price_by_country(self, country):
        country = country[0].capitalize() + country[1:]
        data = self.retail_prices[self.retail_prices['Area'] == country]
        years = data["Year"].tolist()
        values = data["Value"].tolist()
        final_data = {
            "years": years,
            "values": values
        }
        return dumps(final_data)

    def anemia_by_country_by_year(self, country, year):
        country = country[0].capitalize() + country[1:]
        data = self.wasting[self.wasting['country'] == country]
        disaggregation = data["disaggregation"].tolist()
        disaqqvalue = data["disagg.value"].tolist()
        adult_anemia_2000 = data["adult_anemia_2000"].tolist()
        adult_anemia_2001 = data["adult_anemia_2001"].tolist()
        adult_anemia_2002 = data["adult_anemia_2002"].tolist()
        adult_anemia_2003 = data["adult_anemia_2003"].tolist()
        adult_anemia_2004 = data["adult_anemia_2004"].tolist()
        adult_anemia_2005 = data["adult_anemia_2005"].tolist()
        adult_anemia_2006 = data["adult_anemia_2006"].tolist()
        adult_anemia_2007 = data["adult_anemia_2007"].tolist()
        adult_anemia_2008 = data["adult_anemia_2008"].tolist()
        adult_anemia_2009 = data["adult_anemia_2009"].tolist()
        adult_anemia_2010 = data["adult_anemia_2010"].tolist()
        adult_anemia_2011 = data["adult_anemia_2011"].tolist()
        adult_anemia_2012 = data["adult_anemia_2012"].tolist()
        adult_anemia_2013 = data["adult_anemia_2013"].tolist()
        adult_anemia_2014 = data["adult_anemia_2014"].tolist()
        adult_anemia_2015 = data["adult_anemia_2015"].tolist()
        adult_anemia_2016 = data["adult_anemia_2016"].tolist()
        adult_anemia_2017 = data["adult_anemia_2017"].tolist()
        adult_anemia_2018 = data["adult_anemia_2018"].tolist()

        final_data = {
            "disaqqvalue": disaqqvalue,
            "values": values
        }
        return dumps(final_data)

    def get_latest_country_populations(self):
        countries = self.population.Area.unique()
        dct = dict()
        for country in countries:
            data = self.population[self.population['Area'] == country]
            max = data.loc[data['Year'].idxmax()]["Value"]
            dct[country] = max
        return dumps(dct)

    def get_latest_country_productions(self):
        countries = self.clean_data.Area.unique()
        dct = dict()
        for country in countries:
            data = self.clean_data[self.clean_data['Area'] == country]
            max = data.loc[data['Year'].idxmax()]["Value"]
            if max == max:
                dct[country] = max
        return dumps(dct)

    def get_latest_country_prices(self):
        countries = self.prices.Area.unique()
        dct = dict()
        for country in countries:
            data = self.prices[self.prices['Area'] == country]
            max = data.loc[data['Year'].idxmax()]["Value"]
            if max == max:
                dct[country] = max
        return dumps(dct)

    def get_latest_country_wasting(self):
        countries = self.wasting['Countries and areas'].unique()
        dct = dict()
        for country in countries:
            data = self.wasting[self.wasting['Countries and areas'] == country]
            max = data.iloc[0]['Point Estimate']
            if max == max:
                dct[country] = max
        return dumps(dct)


if __name__ == '__main__':
    datasupplier = DataSupplier()
    # print(datasupplier.get_supply_data_by_country("Afghanistan"))
    # print(datasupplier.get_per_person_per_country("Afghanistan"))
    # print(datasupplier.protein_consumption_by_country("India"))
    # print(datasupplier.egg_price_by_country("India"))
    # print(datasupplier.population_by_country("Afghanistan"))
    # print(datasupplier.stunting_by_country("Afghanistan"))
    # print(datasupplier.wasting_by_country("Afghanistan"))
    # print(datasupplier.retail_price_by_country("Afghanistan"))
    print(datasupplier.get_latest_country_populations())
    print(datasupplier.get_latest_country_productions())
    print(datasupplier.get_latest_country_productions()[4160:4170])
    print(datasupplier.wasting_by_country("Afghanistan"))
    print(datasupplier.get_latest_country_wasting())
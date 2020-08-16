from flask import Flask, render_template
from flask_cors import CORS

from DataSupplier import DataSupplier

data_supplier = DataSupplier()
app = Flask(__name__)
CORS(app)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/supply/bycountry/<country>', methods=['POST', 'GET'])
def get_supply(country):
    # if request.method == 'POST':
    return data_supplier.get_supply_data_by_country(country)


@app.route('/perperson/bycountry/<country>', methods=['POST', 'GET'])
def get_perperson(country):
    # if request.method == 'POST':
    return data_supplier.get_per_person_per_country(country)


@app.route('/protein/bycountry/<country>', methods=['POST', 'GET'])
def get_protein(country):
    # if request.method == 'POST':
    return data_supplier.protein_consumption_by_country(country)


@app.route('/price/bycountry/<country>', methods=['POST', 'GET'])
def get_price(country):
    # if request.method == 'POST':
    return data_supplier.egg_price_by_country(country)


@app.route('/population/bycountry/<country>', methods=['POST', 'GET'])
def get_population(country):
    data_supplier.population_by_country(country)


@app.route('/wasting/bycountry/<country>', methods=['POST', 'GET'])
def get_wasting_by_country(country):
    return data_supplier.wasting_by_country(country)


@app.route('/stunting/bycountry/<country>', methods=['POST', 'GET'])
def get_stunting_by_country(country):
    return data_supplier.stunting_by_country(country)


@app.route('/population/all')
def get_all_countries_populations():
    return data_supplier.get_latest_country_populations()


@app.route('/production/all')
def get_all_countries_productions():
    return data_supplier.get_latest_country_productions()


@app.route('/prices/all')
def get_all_countries_prices():
    return data_supplier.get_latest_country_prices()


@app.route('/wasting/all')
def get_wastings():
    return data_supplier.get_latest_country_wasting()


@app.route('/stunting/all')
def get_stuntings():
    return data_supplier.get_latest_country_stunting()


if __name__ == '__main__':
    app.run(debug=True)

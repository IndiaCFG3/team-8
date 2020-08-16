from flask import Flask, render_template

from DataSupplier import DataSupplier

data_supplier = DataSupplier()
app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)

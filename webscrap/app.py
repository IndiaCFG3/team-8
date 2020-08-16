from flask import Flask, render_template

from DataSupplier import DataSupplier

data_supplier = DataSupplier()
app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/supply/bycountry/<country>', methods=['POST', 'GET'])
def get_data(country):
    # if request.method == 'POST':
    return data_supplier.get_supply_data_by_country(country)


@app.route('/perperson/bycountry/<country>', methods=['POST', 'GET'])
def get_data(country):
    # if request.method == 'POST':
    return data_supplier.get_per_person_per_country(country)


@app.route('/protein/bycountry/<country>', methods=['POST', 'GET'])
def get_data(country):
    # if request.method == 'POST':
    return data_supplier.protein_consumption_by_country(country)


if __name__ == '__main__':
    app.run(debug=True)

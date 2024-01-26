from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_car_models', methods =['GET'])
def get_car_models():

    response = jsonify({
        'car_models': util.get_car_models()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_car_price', methods = ['POST'])
def predict_car_price():

    car_model = request.form['car_model']
    year = int(request.form['year'])
    km_driven = int(request.form['km_driven'])
    fuel = request.form['fuel']
    seller = request.form['seller']
    transmission = request.form['transmission']
    owner = request.form['owner']

    response = jsonify({
        'estimated_price': util.get_estimated_price(car_model, year, km_driven, fuel, seller, transmission, owner)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print('Starting Python Flask server for used cars prediction...')
    util.load_artifacts()
    app.run()
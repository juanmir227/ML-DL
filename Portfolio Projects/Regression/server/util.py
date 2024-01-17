import json
import pickle
import numpy as np

__car_models = None
__data_columns = None
__model = None

def get_estimated_price(car_model, year, km_driven, fuel, seller, transmission, owner):
    try:
        car_model_loc_index = __data_columns.index('name_' + car_model.lower())
    except:
        car_model_loc_index = -1
    try:
        fuel_loc_index = __data_columns.index('fuel_' + fuel.lower())
    except:
        fuel_loc_index = -1
    try:
        seller_loc_index = __data_columns.index('seller_type_' + seller.lower())
    except:
        seller_loc_index = -1
    try:
        transmission_loc_index = __data_columns.index('transmission_' + transmission.lower())
    except:
        transmission_loc_index = -1
    try:
        owner_loc_index = __data_columns.index('owner_' + owner.lower())
    except:
        owner_loc_index = -1
    
    X = np.zeros(len(__data_columns))
    X[0] = year
    X[1] = km_driven

    if car_model_loc_index >= 0:
        X[car_model_loc_index] = 1
    if fuel_loc_index >= 0:
        X[fuel_loc_index] = 1
    if seller_loc_index >= 0:
        X[seller_loc_index] = 1
    if transmission_loc_index >= 0:
        X[transmission_loc_index] = 1
    if owner_loc_index >= 0:
        X[owner_loc_index] = 1
    
    return round(__model.predict([X])[0],2)


def load_artifacts():
    print('loading saved artifacts...')
    global __data_columns
    global __car_models

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __car_models = __data_columns[13:]
    global __model
    with open('./artifacts/used_cars_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print('loading saved artifacts...done')

def get_car_models():
    return __car_models

def get_data_columns():
    return __data_columns

if __name__ =='__main__':
    load_artifacts()
    print(get_estimated_price('Maruti 800 AC', 2007, 70000, 'Petrol', 'Individual', 'Manual', 'First owner')) #real 833.0
    # print(get_estimated_price('Hyundai Verna 1.6 SX', 2012, 100000, 'Diesel', 'Individual', 'Manual', 'First Owner')) #real 8333.0
    # print(get_estimated_price('Hyundai i20 Magna 1.4 CRDi (Diesel)', 2014, 80000, 'Diesel', 'Individual', 'Manual', 'Second Owner')) #real 5694.0
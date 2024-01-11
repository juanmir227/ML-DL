import json

__car_models = None
__data_columns = None
__model = None

def get_car_models():
    pass


def load_artifacts():
    print('loading saved artifacts...')
    global __data_columns
    global __car_models

    with open('.artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']


if __name__ =='__main__':
    print(get_car_models())
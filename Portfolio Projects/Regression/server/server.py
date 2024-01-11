from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'This is my page'

if __name__ == '__main__':
    print('Starting Python Flask server for used cars prediction...')
    app.run()

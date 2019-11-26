#!/usr/bin/env python3
from flask import Flask, jsonify, abort, request, make_response, url_for
import json
app = Flask(__name__, static_url_path = "")

    
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

current_temp = 69
current_setpoint = 65
    
@app.route('/governor/api/v1.0/current-temp', methods = ['GET'])
def get_temp():
    return jsonify( { 'current_temp': current_temp})

@app.route('/governor/api/v1.0/current-setpoint', methods = ['GET'])
def get_setpoint():
    return jsonify( { 'current_setpoint': current_setpoint } ) 


@app.route('/governor/api/v1.0/current-setpoint', methods = ['PUT'])
def update_setpoint():
    global current_setpoint
    current_setpoint = json.loads(request.json)['setPoint']
    return jsonify( { 'current_setpoint': current_setpoint } ) 
    

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')

from flask import Flask
from src import status

app = Flask(__name__)

COUNTERS = {}


# POST method to create a counter
@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a counter"""
    app.logger.info(f"Request to create counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        return {"Message": f"Counter {name} already exists"}, status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED


# PUT method to update the counter
@app.route('/counters/<name>', methods=['PUT'])
def update_counter(name):
    app.logger.info(f"Request to update counter: {name}")
    if name not in COUNTERS:
        return {"Message": f"Counter {name} doesnt exists"}, status.HTTP_404_NOT_FOUND
    COUNTERS[name] += 1
    return {name: COUNTERS[name]}, status.HTTP_200_OK


# GET method to read the counter
@app.route('/counters/<name>', methods=['GET'])
def read_counter(name):
    app.logger.info(f"Request to read counter: {name}")
    if name not in COUNTERS:
        return {"Message": f"Counter {name} doesnt exists"}, status.HTTP_404_NOT_FOUND
    return {name: COUNTERS[name]}, status.HTTP_200_OK


# DELETE method to delete the counter
@app.route('/counters/<name>', methods=['DELETE'])
def delete_counter(name):
    app.logger.info(f"Request to delete counter: {name}")
    if name not in COUNTERS:
        return {"Message": "Counter does not exist"}, status.HTTP_404_NOT_FOUND
    del COUNTERS[name]
    return '', status.HTTP_204_NO_CONTENT

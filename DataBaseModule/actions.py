# This file contains implementaions of different actions that can be triggered 
# after reaching specific endpoints

from flask import jsonify

# An action for debugging purposes
def testAction():
    return jsonify({'app' : 'alloy', 'working_status' : True})

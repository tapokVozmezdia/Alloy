# This file contains implementaions of different actions that can be triggered 
# after reaching specific endpoints

from flask import jsonify, request
import dbhandler

# An action for debugging purposes
def testAction():
    return jsonify({'app' : 'alloy', 'working_status' : True})

# An action for getting a table signature (colnames, types)
def getTableStruct(defaults : dict):
    
    # The 'defaults' arg contains 
    
    handler = defaults['handler']

    try:

        table_name = request.args.get('name')
        res = handler.getTableStructure(table_name=table_name)
    
    except Exception as e:  

        print(e)

        res = {'bad args' : 'name'}

    
    return jsonify(res)

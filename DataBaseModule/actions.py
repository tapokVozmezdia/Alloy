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

# Executes a query via given DBHandler object and returns the result
def executeQuery(defaults : dict):

    # for debug purposes
    print('ENTERED THE EXECUTION')
    
    handler = defaults['handler']

    try:

        content = request.data

        if 'query' not in content:
            return jsonify({'error' : 'bad request'})

        query = content['query']

        print(query)
        
        if 'commit' in requests.args:
            
            commit_line = requests.args.get('commit')
            if commit_line.upper() == 'TRUE':
                commit = True
            else:
                commit = False

        else:
        
            commit = False
        
        # for debug purposes
        print(f"commit arg exists: {commit}")

        handler.executeQuery(query=query, commit=commit)

        res = handler.fetchQueryResult()

    except Exception as e:
        
        print(e)

        res = {'critical error' : 'dbhandler'}

    return jsonify(res)


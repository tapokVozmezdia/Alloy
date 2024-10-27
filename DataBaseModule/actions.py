# This file contains implementaions of different actions that can be triggered 
# after reaching specific endpoints

from flask import jsonify, request

import json
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
# !! requires payload to be delivered in a json format, 
# preferably with json.dumps !!
def executeQuery(defaults : dict):

    # for debug purposes
    print('EXECUTE CALLED')
    
    handler = defaults['handler']

    try:
        
        content = json.loads(request.data)
        
        #content = dict(content)
        #print(content)

        if 'query' not in content:
            return jsonify({'error' : 'bad request'})
        
        query = content['query']
        #query = "SELECT * FROM test;"
        
        print(query)
        
        if 'commit' in request.args:
            
            commit_line = request.args.get('commit')
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


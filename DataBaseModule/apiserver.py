# An implementation of an internal API server based on a flask wrapper
# For specifics chech *TODO* file

import os
import json

from flask import Flask, request

import actions
import dbhandler
import flaskwrapper

class Server:
    
    def __init__(self) -> None:

        flask_app = Flask('flask_case')
        self.app = flaskwrapper.FlaskAppWrapper(flask_app)

        # this is so json can always open without trouble
        shift = (len(__name__) + 3) * -1
        config_path = (os.path.realpath(__file__))[:shift] + 'config.json'
        # print(f"config path(api):\n{config_path}")

        with open(config_path, 'r') as conf:
            params = json.load(conf)

        self.handler = dbhandler.DBHandler(params=params)

    def enableGetActions(self) -> None:
        
        self.app.addEndpoint(actions.testAction, '/api/v1/test', 'test', 
            methods=['GET'])
        self.app.addEndpoint(actions.getTableStruct, '/api/v1/tableStruct', 
            'tableStruct', methods=['GET'], defaults={'handler' : self.handler})
    
    def enablePutActions(self) -> None:
        
        self.app.addEndpoint(actions.executeQuery, '/api/v1/execute', 'execute',
            methods=['GET','POST','PUT'], defaults={'handler' : self.handler})    

    def run(self, debug : bool = True) -> None:
        
        self.app.run(debug=debug, port=49599)

    def __del__(self) -> None:
        pass


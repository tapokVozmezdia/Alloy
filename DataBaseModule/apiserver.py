# An implementation of REST API server based on a flask wrapper

from flask import Flask

import actions
import flaskwrapper

class Server:
    
    def __init__(self) -> None:

        flask_app = Flask('flask_case')
        self.app = flaskwrapper.FlaskAppWrapper(flask_app)

    def enableGetActions(self) -> None:
        
        self.app.addEndpoint('/test', 'test', actions.testAction, methods=['GET'])

    def run(self, debug : bool = True) -> None:
        
        self.app.run(debug=debug, port=49599)

    def __del__(self) -> None:
        pass


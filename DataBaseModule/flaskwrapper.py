from flask import Flask

# This is a flask app wrapper made for convinience 
class FlaskAppWrapper:
    
    def __init__(self, app, **configs) -> None:
        
        self.app = app
        self.configs(**configs)

    def __del__(self) -> None:
        pass

    def configs(self, **configs) -> None:
        
        for config, value in configs:
            self.app.config[config.upper()] = value    

    def addEndpoint(self, view_func, endpoint=None, endpoint_name=None, 
        methods=['GET'], **defaults):
        
        self.app.add_url_rule(endpoint, endpoint_name, 
            view_func=view_func, defaults=defaults)

    def run(self, **kwargs):
        
        self.app.run(**kwargs)


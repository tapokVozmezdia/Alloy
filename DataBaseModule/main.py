# This file represents the entry point for running the REST API server,
# It DOES NOT represent the entry point for the entire app

import apiserver
import dbhandler
import json 

def main():

    with open('config.json', 'r') as conf:
        params = json.load(conf)

    # handler = dbhandler.DBHandler(params=params, debug=True)
    
    server = apiserver.Server()
    
    server.enableGetActions()

    server.run()

#entry point
if __name__ == '__main__':
    main()

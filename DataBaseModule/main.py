# This file represents the entry point for running the REST API server,
# It DOES NOT represent the entry point for the entire app

import os
import json

import apiserver
import dbhandler

def main():

    # this is so json can always open without trouble
    config_path = (os.path.realpath(__file__))[:-7] + 'config.json'
    # print(f"config path:\n{config_path}")

    with open(config_path, 'r') as conf:
        params = json.load(conf)

    # handler = dbhandler.DBHandler(params=params, debug=True)
    
    server = apiserver.Server()
    
    server.enableGetActions()

    server.run()

#entry point
if __name__ == '__main__':
    main()

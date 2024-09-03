#!/bin/bash

# This is a script for the separate launch of the database module,
# with working REST API on localhost.
# For specifics check the README file

# This script automatically creates python venv and downloads the needed packages.
# If you have no intentions of altering the script or running the module manually, 
# you can stop reading this file.

# To run the db module, you'll need to have these python packages 
# installed on your machine:
# psycopg2, flask

# It is preferable to run the db module in a separate python virtual enviorment.
# To create one on a linux machine, type this line into the terminal: 
# python3 -m path/to/venv

ENVS_PATH="/opt/alloy/envs"
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if [ ! -d ${ENVS_PATH}/postgresandapi/bin ] || [ ! -f ${ENVS_PATH}/postgresandapi/bin/activate ]; then 
    echo "Standart python venv for the module not found.\n Creating a new venv at ${ENVS_PATH}"
    mkdir -p ${ENVS_PATH}
    python3 -m venv ${ENVS_PATH}/postgresandapi
fi

source ${ENVS_PATH}/postgresandapi/bin/activate
pip install psycopg2
pip install flask

python3 ${SCRIPT_DIR}/DataBaseModule/main.py 

#echo ${SCRIPT_DIR}

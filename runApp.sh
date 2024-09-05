#!/bin/bash

# THIS IS AN OBSOLETE TEMPLATE, SOON TO BE REMADE

# some magic bullshit so that the script can see global aliases
shopt -s expand_aliases
source /root/.bashrc

# getting out of any established python enviorments
# deactivate
# look at the end of the file

# activating postgres enviorment
source /py_env/postgres/bin/activate

# run the program
py main.py

# getting out of postres enviorment
# deactivate
#
# for some reason this shit doesn't work,
# i really couldn't give two fucks about fixing it

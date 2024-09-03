import dbhandler

def main():

    params = {
        'db_name' : 'alloy',
        'db_user' : 'postgres',
        'db_password' : 'postgres',
        'db_host' : 'localhost'
    }

    handler = dbhandler.DBHandler(params=params, debug=True)

    handler.printTable("test")

    

# point of entry
if __name__ == '__main__':
    main()

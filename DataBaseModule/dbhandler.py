import psycopg2


# A custom exception just for this project
def throwException(exception_text : str) -> None:
    print(f"Exception raised in database handler routine.\nMessage:<{exception_text}>.")
    exit(1)

# All interaction with the db is encapsulated into this class
class DBHandler:
    
    def __init__(self, params : dict, debug : bool = False) -> None:

        if (
            'db_name' not in params or
            'db_user' not in params or
            'db_password' not in params or
            'db_host' not in params
        ):
            throwException("""
                invalid parameters given, 
                impossible to establish connection
            """)
        
        self._conn = psycopg2.connect(
            database=params['db_name'],
            user=params['db_user'],
            password=params['db_password'],
            host=params['db_host']
        )

        self._curs = self._conn.cursor()
        self._params = params
        self._debug = debug

        if (self._debug):
            print(f"""
                Connection with the database {params['db_name']} 
                established successfully
            """)

    # Commits all changes and closes connection
    def __del__(self):
    
        self._conn.commit()
        self._curs.close()
        self._conn.close()

        if (self._debug):
            print(f"""
                Connection with the database {self._params['db_name']} 
                terminated successfully
            """)

    # This method also automatically commits changes to the DB
    # To execute a query without commiting it, set commit=False upon calling
    def executeQuery(self, query : str, commit : bool = True) -> None:
        
        self._curs.execute(query)

        if (commit):

            self._conn.commit()
            
            if (self._debug):
                print (f"Query successfully committed:\n{query}")

    # This method returns the first line_num rows of the query result.
    # If line_num = -1 (default value), the method returns a full list
    def fetchQueryResult(self, line_num : int = -1) -> list:
        
        result = self._curs.fetchall()
        
        if (line_num > len(result) or line_num < 0):
            line_num = len(result)

        result = result[:line_num]

        return result

    # This method also empties the query tool buffer 
    def printQueryResult(self) -> None:
        
        colnames = [desc[0] for desc in self._curs.description]
        result = self._curs.fetchall()

        print("")
        for attr_name in colnames:
            print(attr_name, end='\t')
        print("\n")            

        for entry in result:
            for attr in entry:
                print(attr, end='\t')
            print("")
        print("")

    # This method returns names and types of the attributes of the table entries
    # Example: (id : INT), (entry : TEXT)
    def printTableSctructure() -> None:
        pass
        # todo
                    
    # This method prints out the ENTIRE table, 
    # please use with caution for tables with large number of entries
    def printTable(self, table_name : str) -> None:
            
        query = f"SELECT * FROM {table_name};"
        self.executeQuery(query)
        self.printQueryResult()
        

    

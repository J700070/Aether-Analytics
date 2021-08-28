import psycopg2
from config import config

stock = []

def connect(ticker):
    connection = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)
		
        # create a cursor
        c = connection.cursor()
        
        # execute statements
	
        c.execute('SELECT "tickerDate", ticker, date, revenue, "operatingIncome", "netIncome", eps, dividends, "payoutRatio", shares, "bookValue", "bookValuePerShare", "operatingCashFlow", "capSpending", "freeCashFlow", "freeCashFlowPerShare", "workingCapital" FROM public.financials WHERE ticker = \''+ ticker +'\';')
  
        stock = c.fetchall()
       

	# close the communication with the PostgreSQL
        c.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')

    return stock


if __name__ == '__main__':
    connect()
import psycopg2
from config import config

stock = []

def countIndustries():
    connection = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)
		
        # create a cursor
        c = connection.cursor()
        
        # STATEMENTS
        # Returns all financials rows
        #getFinancials = 'SELECT "tickerDate", ticker, date, revenue, "operatingIncome", "netIncome", eps, dividends, "payoutRatio", shares, "bookValue", "bookValuePerShare", "operatingCashFlow", "capSpending", "freeCashFlow", "freeCashFlowPerShare", "workingCapital" FROM public.financials WHERE ticker = \''+ ticker +'\';'
        #Returns the industry list without duplicates
        getIndustryList = 'SELECT DISTINCT ON (industry) industry FROM public.stocks ORDER BY industry ASC;'
        #Returns the number of stocks in an industry
        countIndustryStocks = "SELECT COUNT(industry) FROM public.stocks WHERE industry = '{}';"

        c.execute(getIndustryList)
        industryList = c.fetchall()

        count = []
        industryList = [industry[0] for industry in industryList]
        for industry in industryList:
            c.execute(countIndustryStocks.format(industry))
            count.append((c.fetchall())[0][0])
            
       

	# close the communication with the PostgreSQL
        c.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')

    return industryList, count


if __name__ == '__main__':
    countIndustries()
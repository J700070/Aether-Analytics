from database import countIndustries
import numpy as np

def getStock(ticker):

    rawStock = connect(ticker)

    entryCount = 0
    maxEntryCount = len(rawStock)

    #Morningstar Financials
    ticker = rawStock[0][1]
    dates = [None]*maxEntryCount
    revenue = [None]*maxEntryCount
    operatingIncome = [None]*maxEntryCount
    netIncome = [None]*maxEntryCount
    eps = [None]*maxEntryCount
    dividends = [None]*maxEntryCount
    payoutRatio = [None]*maxEntryCount
    shares = [None]*maxEntryCount
    bookValue = [None]*maxEntryCount
    bookValuePerShare = [None]*maxEntryCount
    operatingCashFlow = [None]*maxEntryCount
    capSpending = [None]*maxEntryCount
    freeCashFlow = [None]*maxEntryCount
    freeCashFlowPerShare = [None]*maxEntryCount
    workingCapital = [None]*maxEntryCount


    for entry in rawStock:

        dates[entryCount] = entry[2]
        revenue[entryCount] = entry[3]
        operatingIncome[entryCount] = entry[4]
        netIncome[entryCount] = entry[5]
        eps[entryCount] = entry[6]
        dividends[entryCount] = entry[7]
        payoutRatio[entryCount] = entry[8]
        shares[entryCount] = entry[9]
        bookValue[entryCount] = entry[10]
        bookValuePerShare[entryCount] = entry[11]
        operatingCashFlow[entryCount] = entry[12]
        capSpending[entryCount] = entry[13]
        freeCashFlow[entryCount] = entry[14]
        freeCashFlowPerShare[entryCount] = entry[15]
        workingCapital[entryCount] = entry[16]


        entryCount+=1


            
    stock = {
        "ticker": ticker,
        "dates": dates,
        "revenue": revenue,
        "operatingIncome": operatingIncome,
        "netIncome": netIncome,
        "eps": eps,
        "dividends": dividends,
        "payoutRatio": payoutRatio,
        "shares": shares,
        "bookValue": bookValue,
        "bookValuePerShare": bookValuePerShare,
        "operatingCashFlow": operatingCashFlow,
        "capSpending": capSpending,
        "freeCashFlow": freeCashFlow,
        "freeCashFlowPerShare": freeCashFlowPerShare,
        "workingCapital": workingCapital
    }

    return stock


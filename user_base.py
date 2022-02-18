from datetime import datetime
import sys
import requests
import plotext as plt


def getHttpData() -> (dict):
     '''TODO'''
    

def arrangeData(data) -> (list):
    '''TODO'''
    

def dateFilter(dates, start_date, end_date) -> (list):
    '''TODO'''

    start_date = datetime.strptime(start_date, '%d-%m-%Y')
    end_date = datetime.strptime(end_date, '%d-%m-%Y')
    # dates=['4-6-2013', '4-5-2013', '26-6-2013', '26-7-2013', '9-5-2013', '10-7-2013', '12-10-2013', '4-12-2014', '5-10-2014', '6-12-2014', '19-7-2014', '15-8-2014', '17-9-2014', '21-4-2015', '28-5-2015', '26-2-2015']
    return  [date for date in dates if start_date <= datetime.strptime(date, '%d-%m-%Y') <=end_date]

def plotGraph(x, y):
    '''TODO'''


if __name__ == '__main__':
    args = sys.args

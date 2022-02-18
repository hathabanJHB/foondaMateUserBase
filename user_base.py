from datetime import datetime
import sys
import requests
import plotext as plt


def getHttpData() -> (dict):
     '''TODO'''
    

def arrangeData(data) -> (list):
    '''TODO'''
    

def dateFilter(dates, start_date, end_date) -> (list):
    if start_date in dates and end_date in dates:
        start_date = datetime.strptime(start_date, '%d-%m-%Y')
        end_date = datetime.strptime(end_date, '%d-%m-%Y')
        return  [date for date in dates if start_date <= datetime.strptime(date, '%d-%m-%Y') <=end_date]
    return []

def plotGraph(x, y):
    '''TODO'''


if __name__ == '__main__':
    args = sys.args

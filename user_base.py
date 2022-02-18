from datetime import datetime
import sys
import requests
import plotext as plt


def getHttpData(url) -> (str):
    """Makes HTTP GET request to the given url
    and returns response as string.

    Args:
        url (str): url to send GET request to.

    Returns:
        (str): stringfied dictionary or an error message if http response is not (ok)200.
    """   

    err_msg = f"""Error: Unable to get userbase. try the following:
            - check your internet connection
            - check if \"{url}\" is correct
            - retry
                    """  
    try:
        response = requests.get(url)
        return str(response.json())
    except requests.exceptions.ConnectionError as e:
        return err_msg
    

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

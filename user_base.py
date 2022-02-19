from datetime import datetime
import json
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
    """[sorts dates and users]

    Args:
        data [string]: [stringfied dictionary]

    Returns:
        [list]: [users<int>:list containing number of users] [dates<str>:list of dates in a string format]
    """    
    data = data.replace("'",'"') # replace (') with (") so that data can be converted to a dictionary.
    mappedData = json.loads(data)
    sortedData = sorted(mappedData.items()) # sort dictionary by keys
    users =[]
    dates = []

    for i in range(len(sortedData)):
        dates.append(sortedData[i][0])
        users.append(int(sortedData[i][1]))

    return users,dates
    

def dateFilter(dates, start_date, end_date) -> (list):
    """filter date by start date and end date

    Args:
        dates (_type_): _description_
        start_date: (string) dd-mm-yyyy
        end_date: (string) dd-mm-yyyy

    Returns:
        list: list of dates and list of users
    """        
    if start_date in dates and end_date in dates:
        start_date = datetime.strptime(start_date, '%d-%m-%Y')
        end_date = datetime.strptime(end_date, '%d-%m-%Y')
        return  [date for date in dates if start_date <= datetime.strptime(date, '%d-%m-%Y') <=end_date]
    return []


def getArgsDates(dates, args)-> (list): 
    """_summary_

    Args:
        dates (list): _description_
        args (list): _description_

    Returns:
    (list): _description_
    """    
    if len(args) == 5:
        try:
            start_date = [args[i+1] for i in range(len(args)) if args[i] == '-s'][0]
            end_date = [args[i+1] for i in range(len(args)) if args[i] == '-e'][0]
        except IndexError:
            return 0
        try:
            sd = datetime.strptime(start_date, '%d-%m-%Y') #start date
            ed = datetime.strptime(end_date, '%d-%m-%Y') #end date
            assert (sd)
            assert (ed)
            if sd > ed:
                print('Start date should be less than end date')
                return 0
            return [start_date, end_date]
        except ValueError:
            print('Date format should be: dd-mm-yyyy')
            exit()
    elif len(args) == 1:
        return [dates[0], dates[-1]]
    else:
       return 0


def plotGraph(x, y):
    """plots a bar graph on the terminal with given list of coordinates given as arguments .

    Args:
        x (list): list of x-axis data.
        y (list): list of y-axis data.
    """    
    plt.clc() # making the plot colorless; so it adapts to the terminal colors
    plt.title("FOONDAMATE USERBASE")
    plt.bar(y,x)
    plt.show()


def help():
    """_shows help message

    Returns:
        (string): help message
    """    
    return """Tool to visualize User base
    usage: [user_base.py -s 12-11-2002 -e 12-3-2023]
    
    Date format: dd-mm-yyyy
    Start date should be less than end date
    
    -s \t\t start date
    -e \t\t end date"""


if __name__ == '__main__':
    url = 'http://sam-user-activity.eu-west-1.elasticbeanstalk.com/'
    data = getHttpData(url)
    args = sys.argv
    users, dates = arrangeData(data)

    if type(getArgsDates(dates, args)) == list:
        start_date, end_date = getArgsDates(dates, args)
        plotGraph(users, dates)# FoondaMate Software Engineer Coding Challenge-001
CLI application that sends an HTTP request to an end point that returns a userbase (_**Dates as keys and the number of active users on those dates (as values)**_) then plots a bar graph that  visualises the growth of a company. Users can filter the data they want to see by specifying  _start date_ and _end date_.


### The User Base bar graph
* Shows number of users on the y-axis
* Shows dates on the x-axis

## How to install
### Use [Makefile](https://www.gnu.org/software/make/manual/make.html) for configuration

**All required packages are installed in a [virtualenv](https://docs.python.org/3/library/venv.html) to activated the *virtualenv* run:**

> **NOTE**: Use the commands bellow without the dollar sign ($)

```bash
'$make env'
```

**To install all required packages run:**
```bash
'$make install'
```

## Usage
The program runs on the terminal and it takes the following command line argument:
* Start date in (_dd-mm-yy_) format: specified by the `-s` flag
```bash
python3 user_base.py -s 12-11-2002 -e 12-3-2023
```
* End in (_dd-mm-yy_) format

```bash
$python3
```

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
    else:
        print(f'Available dates: ', *dates)
        print()
        print(help())
        exit()


    # print(getArgsDates())

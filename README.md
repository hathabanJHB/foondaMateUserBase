# FoondaMate Software Engineer Coding Challenge-001

CLI application that sends an HTTP request to an end point that returns a userbase (_**Dates as keys and the number of active users on those dates (as values)**_) then plots a bar graph that  visualises the growth of a company. Users can filter the data they want to see by specifying  _start date_ and _end date_.

### The User Base bar graph

* Shows number of users on the y-axis
* Shows dates on the x-axis

## How to install
### Use [Makefile](https://www.gnu.org/software/make/manual/make.html) for configuration

**All required packages are installed in a [virtualenv](https://docs.python.org/3/library/venv.html) to activated the *virtualenv* run:**

> **NOTE**: Use the commands bellow without the dollar sign ($)

```bash
$ make env
```
or
```bash
$ source env/bin/activate
```


**To install all required packages run:**
```bash
$ make install
```
or
```bash
$ pip3 install -r requirements.text
``` 
&nbsp;

## Running unittests
#### Starting the test server
There is a [test server](https://github.com/hathabanJHB/foondaMateUserBase/blob/main/tests/test_server.py) in the [tests directory](https://github.com/hathabanJHB/foondaMateUserBase/tree/main/tests) that help to test the network layer functions. You need to start the server on a separate terminal. Assuming you're in the [base directory](https://github.com/hathabanJHB/foondaMateUserBase/tree/main/) just run:
```bash
$ python3 tests/test_server.py
``` 
or
```bash
$ make runserver
``` 
#### Running all test
> **NOTE**: Some tests will fail if the [test server](https://github.com/hathabanJHB/foondaMateUserBase/blob/main/tests/test_server.py) is not running

```bash
$ make test
``` 
or
```bash
$ python3 -m unittest tests/test_user_base.py
``` 



&nbsp;

## Usage
```bash
$ python3 user_base.py -s start_date -e end_date
```
The program runs on the terminal and it takes the following command line argument:
* Start date in (_dd-mm-yy_) format: specified by the `-s` flag
```bash
$ python3 user_base.py -s 01-01-2022
```
* End in (_dd-mm-yy_) format specified by the `-e` flag

```bash
python3 user_base.py -e 15-01-2022
```
#### example:
```bash
python3 user_base.py -s 01-01-2022 -e 15-01-2022
```
**For any query send Email to: <hthabang23@gmail.com>
# foondaMateUserBase
CLI application that visualises the growth of company userbase by plotting a graph on a terminal

The programs run on virtual enviroment.
    to get all dependancies run:
    make env

!Note you need to run to run the test server in a different terminal to run all the tests
to run all tests:
    make test

To run the test server
    make runserver

to run the program:
    user_base.py -s {start date} -e {end date}
    eg: user_base.py -s 12-11-2002 -e 12-3-2023

to view program requirements:
    make requirements
runserver:
	python3 tests/test_server.py

test:
	python3 -m unittest tests/test_user_base.py

install:
	pip3 install -r requirements.text

env:
	source env/bin/activate
runserver:
	python3 tests/test_server.py

test:
	python3 -m unittest tests/test_user_base.py

requirements:
	python3 -m pip freeze

env:
	source env/bin/activate


	

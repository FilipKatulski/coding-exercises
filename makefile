all: dependencies test-executor build

test: dependencies test-executor

dependencies:
		pip3 install -r requirements.txt

test-executor:
		cd exercise2 && python3 setup.py pytest 

build:
		cd exercise2 && python3 setup.py sdist bdist_wheel

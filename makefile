all: dependencies test-executor build-executor push 

test: dependencies test-executor

build: dependencies build-executor

dependencies:
		pip3 install -r requirements.txt

test-executor:
		cd exercise2 && python3 setup.py pytest 

build-executor:
		cd exercise2 && python3 setup.py sdist bdist_wheel

push:
		cd exercise2 && python3 -m twine upload --repository testpypi dist/* 

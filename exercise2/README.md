# Exercise 2

A python package that returns the structure of a directory, given in the specified JSON format. The package is tested with pytest, tests are located in the [tests](tests) folder. No external libraries are used in the Dependency Tree solution, but pytest is used for testing. The package is installed with the use of the 'setup.py' file.

I store the structure in a object of the DependencyTree class that stores the dependencies structure in an list, where each element is a element of the Tree. Upon printing the object of the DependencyTree class, the structure is printed as a string. 

### Installation

You can install the package with the use of the 'setup.py' file:

```bash
python -m venv .venv
source .venv/bin/activate
python setup.py install
```

Moreover, the package is registered on [TestPyPI](https://test.pypi.org/project/dependencytrees/) and can be installed with the use of pip:

```bash
pip install -i https://test.pypi.org/simple/ dependencytrees
```

### Testing

The package is tested with pytest. To run the tests, please use the following command:

```bash
pytest tests
```

### Usage

By default the code takes an example file located in '/tmp/example1.json'. If you want to use another file, you can specify the path to the file with the '-f' / '--json-file' argument. 

Please use '--help' to see the usage of the program.

Example input file (JSON format):

```
{
    "pkg1": [
        "pkg2",
        "pkg3"
    ],
    "pkg2": [
        "pkg3"
    ],
    "pkg3": []
}
```

Run the code:
    
```bash
python -m dependencytrees [-h] [-f JSON_FILE]
```

Example's output:
```
- pkg1
  - pkg2
    - pkg3
  - pkg3
- pkg2
  - pkg3
- pkg3
```

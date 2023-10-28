from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dependencytrees',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    setup_requires=['pytest-runner==6.0.0'],
    tests_require=['pytest==7.4.3'],
    test_suite='tests',
    author='Filip Katulski',
    author_email='filipkatulski@gmail.com',
    description='Package for creating dependency trees from JSON files.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/your-repo',
)

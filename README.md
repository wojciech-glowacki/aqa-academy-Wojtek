# aqa-academy-Wojtek

# Coding rules
## Excluded folders
1. .venv folder
2. reports folder
In order to avoid conflicts during git push

## Dependency updates
1. Major libs version needs to be revisited once per month

# How-to
1. Setup your env
1.1 Create venv into .venv folder
1.1.1 python -m venv .venv
1.1.2 source .venv/scripts/activate
1.2 Install dependencies from requirements.txt file
1.2.1 pip install -r requirements.txt

2. Before commit
2.1 Run black formatter [https://pypi.org/project/black/]
2.2 Run flake8 tool [https://pypi.org/project/flake8/]
2.3 Run isort tool [https://pypi.org/project/isort/]

3. Run the tests
3.1 Run the tests with additional results information
3.1.1 pytest . -s -v (in the root of the framework)
3.2 Run the tests and generate a report
3.2.1 pytest --html=reports/report.html --self-contained-html

# Structure of the framework
1. tests - folder for tests
2. reports - folder for local reports
3. src/applications - folder for system under test abstractions
4. src/config - folder for configuration of framework
5. src/helpers - folder for single-use functions, etc

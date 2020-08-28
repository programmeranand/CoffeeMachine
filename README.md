# CoffeeMachine
Simulates a Coffee Machine, having various outlets, each outlet serving different type of beverage using different ingredients

## Prerequisites
    Python 3.6+
    UNIX operating System
    
## How to run?
    1. Create a Virtual env as `python3 -m venv <VIRTUAL_ENV_NAME>`
        1.1 Change directory to the env `cd <VIRTUAL_ENV_NAME>`
    2. Clone the Repository inside Virtual environment :-  `git clone git@github.com:programmeranand/CoffeeMachine.git`
        2.1 Activate virtual environment `source bin/activate`
        2.2 Change Directory to cloned repo `cd CoffeeMachine`
    3. Run `main.py` file as `python3 main.py`

## How to run tests?
    1. Run `python3 -m unittest CoffeeMaker/tests/test_coffee_machine.py` to run tests
    2. Additional test data are provided in `test_data.json` and `test_data2.json`
import os
from CoffeeData.data import CoffeeMachineData
from CoffeeMaker.machine import CoffeeMachine


def main():
    """
    Invokes CoffeeMachine, initializes ingredients based on the data given
    :return:
    """
    # Read coffee Machine data

    # Define input data directory
    input_data_directory = 'CoffeeData'

    # Define input file name
    input_filename = 'input.json'
    input_path = os.path.dirname(os.path.abspath(__file__)) + '/' + input_data_directory + '/' + input_filename

    # Parse given input data
    data_client = CoffeeMachineData()
    parsed_data = data_client.parse_input_file(input_path)

    # Invoke Coffee Machine for operation
    coffee_machine = CoffeeMachine()
    coffee_machine.prepare_outlets(parsed_data['total_outlets'])
    coffee_machine.add_ingredients(parsed_data['total_items_quantity'])
    for beverage, ingredients in parsed_data['beverages'].items():
        coffee_machine.queue.put((beverage, ingredients))

    # Prepare beverages
    coffee_machine.queue.join()

    # Check Low ingredient status
    coffee_machine.status()

    # Refill ingredients with low status
    coffee_machine.refill_machine()


if __name__ == "__main__":
    main()

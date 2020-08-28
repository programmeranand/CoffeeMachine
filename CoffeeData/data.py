import json


class CoffeeMachineData(object):
    def __init__(self):
        self.total_outlets = 0
        self.total_items_quantity = {}
        self.beverages = {}

    def parse_input_file(self, input_path):
        """
        Reads and Parses input file data
        """
        with open(input_path) as input_json_data:
            input_data = json.load(input_json_data)

        self.total_outlets = input_data['machine']['outlets']['count_n']
        self.total_items_quantity = input_data['machine']['total_items_quantity']
        self.beverages = input_data['machine']['beverages']

        parsed_data = {
            'total_outlets': self.total_outlets,
            'total_items_quantity': self.total_items_quantity,
            'beverages': self.beverages
        }

        return parsed_data

import os
import unittest

from CoffeeData.data import CoffeeMachineData
from CoffeeMaker.machine import CoffeeMachine


class CoffeeMachineTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        self.test_input_data_directory = 'CoffeeData'
        self.test_input_filename1 = 'test_data.json'
        self.test_input_filename2 = 'test_data2.json'
        self.test_input_file_path1 = os.path.dirname(
            os.path.abspath(__file__)) + '/' + '../../CoffeeData/' + self.test_input_filename1
        self.test_input_file_path2 = os.path.dirname(
            os.path.abspath(__file__)) + '/' + '../../CoffeeData/' + self.test_input_filename2

    def test_coffee_machine_sample_data(self):
        test_data_client = CoffeeMachineData()
        test_parsed_data1 = test_data_client.parse_input_file(self.test_input_file_path1)

        test_coffee_machine1 = CoffeeMachine()
        test_coffee_machine1.prepare_outlets(test_parsed_data1['total_outlets'])
        test_coffee_machine1.add_ingredients(test_parsed_data1['total_items_quantity'])
        for beverage, ingredients in test_parsed_data1['beverages'].items():
            test_coffee_machine1.queue.put((beverage, ingredients))

        with self.assertLogs('CoffeeMaker.machine', level="INFO") as logger:
            test_coffee_machine1.queue.join()
            test_coffee_machine1.status()
            test_coffee_machine1.refill_machine()
            self.assertEqual(logger.records[0].msg, "hot_tea is prepared")
            self.assertEqual(logger.records[1].msg, "hot_coffee is prepared")
            self.assertEqual(logger.records[2].msg, "black_tea is prepared")
            self.assertEqual(logger.records[3].msg, "green_tea is prepared")
            self.assertEqual(logger.records[4].msg, "Kindly Refill hot_milk, ginger_syrup")
            self.assertEqual(logger.records[5].msg, "hot_milk refilled to capacity: 500")

        test_parsed_data2 = test_data_client.parse_input_file(self.test_input_file_path2)
        test_coffee_machine2 = CoffeeMachine()
        test_coffee_machine2.prepare_outlets(test_parsed_data2['total_outlets'])
        test_coffee_machine2.add_ingredients(test_parsed_data2['total_items_quantity'])
        for beverage, ingredients in test_parsed_data2['beverages'].items():
            test_coffee_machine2.queue.put((beverage, ingredients))

        with self.assertLogs('CoffeeMaker.machine', level="INFO") as logger:
            test_coffee_machine2.queue.join()
            test_coffee_machine2.status()
            test_coffee_machine2.refill_machine()
            self.assertEqual(logger.records[0].msg, "green_tea is prepared")
            self.assertEqual(logger.records[1].msg, "hot_tea is prepared")
            self.assertEqual(logger.records[2].msg, "hot_coffee cannot be prepared as hot_milk is not enough")
            self.assertEqual(logger.records[3].msg, "black_tea is prepared")
            self.assertEqual(logger.records[4].msg, "No ingredient at low levels at the moment")

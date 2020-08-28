import logging
from queue import Queue

from CoffeeMaker.bucket import Bucket
from CoffeeMaker.exceptions import IngredientDoesNotExist, NotEnoughIngredient
from CoffeeMaker.outlet import Outlet

logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s] [%(asctime)s] [%(name)s] [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger(__name__)


class CoffeeMachine(object):
    """Class to Simulate the behaviour of Coffee Machine
        Here we are using a Queue to simulate the behaviour of orders for different beverages
    """
    def __init__(self):
        self.queue = Queue()
        self.ingredients = {}
        self.outlets = 0

    def add_ingredients(self, ingredients):
        """
        Adds ingredients to the machine
        :param ingredients: ingredients to add to the coffee machine
        """
        for ingredient, capacity in ingredients.items():
            self.ingredients[ingredient] = Bucket(ingredient_name=ingredient, capacity=capacity)

    def prepare_outlets(self, outlets):
        """
        Sets the number of outlets on the machine
        :param outlets: number of outlets on the machine
        :return: None
        """
        self.outlets = outlets
        for _ in range(self.outlets):
            worker = Outlet(self.queue, self.prepare_beverage)
            worker.daemon = True
            worker.start()

    def prepare_beverage(self, beverage, ingredients):
        """
        Prepares the beverage
        :param beverage: beverage to be prepared
        :param ingredients: ingredients required to prepare the beverage
        """
        try:

            # First we need to check if all the ingredients are there
            for ingredient, quantity in ingredients.items():
                if self.ingredients.get(ingredient, None) is None:
                    raise IngredientDoesNotExist(ingredient)
                else:
                    ingredient_container = self.ingredients[ingredient]
                    try:
                        ingredient_container.check_ingredient(quantity=quantity)
                    except NotEnoughIngredient as e:
                        raise e

            # Once we have verified all the ingredients are there, we can prepare the beverage
            for ingredient, quantity in ingredients.items():
                ingredient_bucket = self.ingredients[ingredient]
                ingredient_bucket.use_ingredient(quantity=quantity)

            logger.info(f'{beverage} is prepared')

        except IngredientDoesNotExist as e:
            logger.error(f'{beverage} cannot be prepared bacause {str(e)} is not available')
        except NotEnoughIngredient as e:
            logger.error(f'{beverage} cannot be prepared as {str(e)} is not enough')

    def status(self):
        """
        Shows the status of ingredients that need filling
        :return: Boolean if any ingredient has to be filled
        """
        refill = []
        for ingredient in self.ingredients.values():
            if ingredient.status_indicator():
                refill.append(ingredient.ingredient_name)
        if len(refill) > 0:
            logger.info('Kindly Refill ' + ", ".join(refill))
            return True
        else:
            logger.info('No ingredient at low levels at the moment')
            return False

    def refill_machine(self):
        for ingredient_name, ingredient in self.ingredients.items():
            if ingredient.status_indicator():
                ingredient.refill()
                logger.info(f'{ingredient.ingredient_name} refilled to capacity: {ingredient.capacity}')
                # Update the refilled machine in the coffee machine
                self.ingredients[ingredient_name] = ingredient

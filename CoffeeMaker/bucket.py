from CoffeeMaker.exceptions import NotEnoughIngredient


class Bucket(object):
    """
    Bucket class representing individual buckets for holding ingredients
    """
    def __init__(self, ingredient_name, capacity, refill_indication=15):
        """
        Initializes the container for any ingredient
        :param ingredient_name: Name of the ingredient
        :type ingredient_name: string
        :param capacity: Capacity of the ingredient
        :type capacity: integer
        :param refill_indication: the percentage at which low quantity indicator should be shown
        :type refill_indication: integer
        """
        self.capacity = capacity
        self.ingredient_name = ingredient_name
        self.indicate_at = refill_indication
        self.amount = capacity

    def status_indicator(self):
        """
        Indicates if the ingredient is below the indication percentage.
        Returns true if the amount is below the limit.
        :return: Boolean
        """
        return self.indicate_at >= (float(self.amount) / float(self.capacity))*100

    def use_ingredient(self, quantity):
        """
        Utilizes the ingredient quantity specified
        :param quantity: the quantity of the ingredient needed
        :type quantity: integer
        """
        if quantity > self.amount:
            raise NotEnoughIngredient(self.ingredient_name)
        else:
            self.amount = self.amount - quantity

    def check_ingredient(self, quantity):
        """
        Checks if the required quantity of ingredient is available
        :param quantity: the quantity of the ingredient needed
        :type quantity: integer
        :return: Boolean
        """
        if quantity > self.amount:
            raise NotEnoughIngredient(self.ingredient_name)
        else:
            return True

    def refill(self):
        """
        Refills the bucket back upto it's Capacity
        :param quantity: quantity
        :type quantity: integer
        """
        self.amount = self.capacity
        return self.amount

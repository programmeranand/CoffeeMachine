class NotEnoughIngredient(Exception):
    """Exception thrown when ingredient is less than desired quantity required for beverage"""
    def __init__(self, deficient_ingredient: str) -> None:
        super().__init__(deficient_ingredient)
        self.deficient_ingredient = deficient_ingredient


class IngredientDoesNotExist(Exception):
    """Exception thrown when ingredient does not exist in the machine"""
    def __init__(self, missing_ingredient: str) -> None:
        super().__init__(missing_ingredient)
        self.missing_ingredient = missing_ingredient

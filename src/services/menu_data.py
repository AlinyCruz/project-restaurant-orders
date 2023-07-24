import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient

# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self._read_csv_and_create_dishes()

    def _read_csv_and_create_dishes(self) -> None:
        with open(self.source_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            dishes_data = {}  # Dicionário temporário para armazenar os dados dos pratos e suas receitas

            for row in reader:
                dish_name = row['dish']
                dish_price = float(row['price'])
                ingredient_name = row['ingredient']
                recipe_amount = int(row['recipe_amount'])

                if dish_name not in dishes_data:
                    dishes_data[dish_name] = {'price': dish_price, 'recipe': {}}

                dishes_data[dish_name]['recipe'][ingredient_name] = recipe_amount

        # Criar instâncias de pratos (Dish) e ingredientes (Ingredient) e adicioná-los ao conjunto dishes
        for dish_name, dish_data in dishes_data.items():
            dish_ingredients = []
            for ingredient_name, recipe_amount in dish_data['recipe'].items():
                ingredient = Ingredient(ingredient_name)
                dish_ingredients.append((ingredient, recipe_amount))

            dish = Dish(dish_name, dish_data['price'])
            for ingredient, amount in dish_ingredients:
                dish.add_ingredient_dependency(ingredient, amount)

            self.dishes.add(dish)

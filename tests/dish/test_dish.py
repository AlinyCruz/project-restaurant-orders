from src.models.ingredient import Ingredient, Restriction
from src.models.dish import Dish
import pytest

# Req 2
def test_dish():
    dish_lazanha = Dish("lazanha", 25.49)
    dish_pizza = Dish("pizza", 45.00)

    assert dish_lazanha.name == "lazanha"
    assert dish_lazanha.price == 25.49
    assert dish_lazanha.recipe == {}

    assert dish_lazanha.get_ingredients() == set()
    assert dish_lazanha == dish_lazanha
    assert dish_lazanha != dish_pizza

    assert hash(dish_lazanha) == hash(dish_lazanha)
    assert hash(dish_lazanha) != hash(dish_pizza)

    assert repr(dish_lazanha) == "Dish('lazanha', R$25.49)"
    assert repr(dish_lazanha) != "Dish('pizza', R$45.00)"

    dish_lazanha.add_ingredient_dependency(Ingredient("presunto"), 2)

    assert dish_lazanha.get_restrictions() == { Restriction.ANIMAL_DERIVED, Restriction.ANIMAL_MEAT }
    assert dish_lazanha.get_ingredients() == {Ingredient("presunto")}

    with pytest.raises(ValueError):
        Dish("lazanha", -25.90)
    with pytest.raises(TypeError):
        Dish("lazanha", "25.90")
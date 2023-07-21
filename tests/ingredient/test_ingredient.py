from src.models.ingredient import Ingredient,  restriction_map  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("tomate")
    assert isinstance(ingredient, Ingredient)
    assert ingredient.name == "tomate"

    expected_restrictions = restriction_map().get("tomate", set())
    assert ingredient.restrictions == expected_restrictions

    assert repr(ingredient) == "Ingredient('tomate')"

    ingredient1 = Ingredient("tomate")
    ingredient2 = Ingredient("tomate")
    ingredient3 = Ingredient("batata")
    
    assert ingredient1 == ingredient2
    assert not ingredient1 == ingredient3

    ingredient1 = Ingredient("tomate")
    ingredient2 = Ingredient("tomate")
    ingredient3 = Ingredient("batata")

    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)

    assert ingredient.name == "tomate"

    expected_restrictions = restriction_map().get("tomate", set())
    assert ingredient.restrictions == expected_restrictions

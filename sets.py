from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    dish_ing1 = set(dish_ingredients)
    return(dish_name, dish_ing1)


def check_drinks(drink_name, drink_ingredients):
    drin_ing2 = set(drink_ingredients)
    alcohol_1 = set(ALCOHOLS)

    if drin_ing2.intersection(alcohol_1) == set():
        return (str(drink_name) + " " + "Mocktail")
    else:
        return (str(drink_name) + " " + "Cocktail")

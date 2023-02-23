from typing import List

def roll_call_dwarves(dwarves: List[str]) -> None:
    '''prints out the dwarves in a numbered list'''
    for i, name in enumerate(dwarves, start=1):
        print(f"{i}. {name}")

def summon_captain_planet(planeteer_calls: List[str]) -> List[str]:
    '''capitalizes each element and adds an exclamation mark'''
    return [call.capitalize() + '!' for call in planeteer_calls]

def long_planeteer_calls(calls: List[str]) -> bool:
    '''returns True if any calls are longer than 4 characters, False otherwise'''
    return any(len(call) > 4 for call in calls)

def find_the_cheese(ingredients: List[str]) -> str:
    '''returns the first element of the array that is cheese, or None if the array does not contain a type of cheese'''
    cheeses = ['cheddar', 'gouda', 'camembert']
    for ingredient in ingredients:
        if ingredient in cheeses:
            return ingredient
    return None
#GPT REDO GDC 2.23.23
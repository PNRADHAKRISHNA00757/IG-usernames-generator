import random

def hobby_username(hobbies: list) -> str:
    """
    Generates a username based on a given list of hobbies.

    :param hobbies: A list of hobby strings.
    :return: A generated username string.
    """
    hobby = random.choice(hobbies)
    username = f"hobby_{hobby}"
    return username

def animal_username(animals: list) -> str:
    """
    Generates a username based on a given list of animals.

    :param animals: A list of animal strings.
    :return: A generated username string.
    """
    animal = random.choice(animals)
    username = f"animal_{animal}"
    return username
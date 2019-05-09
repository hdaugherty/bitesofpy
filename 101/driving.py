# PyBites Bite 101. f-strings and a simple if/else


MIN_DRIVING_AGE = 18  # Sets the minimum driving age


def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""

    if age < 18:
        print (f"{name} is not allowed to drive")
    if age >= 18:
        print(f"{name} is allowed to drive")

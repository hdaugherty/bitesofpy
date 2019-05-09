MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    if age < 18:
        print (f"{name} is not allowed to drive.")
    if age >= 18:
        print(f"{name} is allowed to drive.")
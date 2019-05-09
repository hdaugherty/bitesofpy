MIN_DRIVING_AGE = 16


def allowed_driving(name, age):
    if age < 16:
        print (f"{name} is not allowed to drive.")
    if age >= 16:
        print(f"{name} is allowed to drive.")
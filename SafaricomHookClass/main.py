from typing import Final, final
from datetime import datetime


# Defining final means the variable can't be changed
PI: Final[str] = '3.142'
print(PI)

site_name = final(str('Power learn project'))
print(site_name)

# Defining the function as  arrow function
def current_datetime() -> None:
    current_time = datetime.now()
    print(f'Current time is: {current_time}')

current_datetime()


# using the params on the function, None is a type definition return value
def arithmetic(a: int, b: int) -> None:
    total = a + b
    total_add = sum([a,b])

    print(f'the sum is: {total} {total_add}')

arithmetic(5,10)

# class, instance of the object self points to the attributes of the object
class Car:
    def __init__(self, color: str, horsepower: int) -> None:
        self.color = color
        self.horsepower = horsepower

    def drive(self) -> None:
        print(f'{self.color} car is being driven')

my_car = Car(color="Red", horsepower=150)
print(f"My car is {my_car.color} and has {my_car.horsepower} horsepower.")

my_car.drive()


def cars_needed(members):
    car_capacity = 4
    cars_needed = (members + car_capacity - 1)//car_capacity
    return cars_needed

members = int(input())
cars_required = cars_needed(members)
print(cars_required)

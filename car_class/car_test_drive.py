from car import Car

car_object = Car(1996, "Toyota Tamaraw FX")

print("Accelerating")

for count in range(5):
    car_object.accelerate()
    print("Current Speed:", car_object.get_speed())

print("\nBraking")

for count in range(5):
    car_object.brake()
    print("Current Speed:", car_object.get_speed())
from fan import Fan

first_fan = Fan(
    Fan.FAST,
    10,
    "yellow",
    True
)

second_fan = Fan(
    Fan.MEDIUM,
    5,
    "blue",
    False
)

print("First Fan")
print("Speed:", first_fan.get_speed())
print("Radius:", first_fan.get_radius())
print("Color:", first_fan.get_color())
print("On:", first_fan.get_fan_on())

print("\nSecond Fan")
print("Speed:", second_fan.get_speed())
print("Radius:", second_fan.get_radius())
print("Color:", second_fan.get_color())
print("On:", second_fan.get_fan_on())
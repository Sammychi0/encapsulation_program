from pet import Pet

pet_object = Pet()

pet_name = input("Enter pet name: ")
animal_type = input("Enter animal type: ")
pet_age = int(input("Enter pet age: "))

pet_object.set_name(pet_name)
pet_object.set_animal_type(animal_type)
pet_object.set_age(pet_age)

print("\nPet Information")
print("Name:", pet_object.get_name())
print("Type:", pet_object.get_animal_type())
print("Age:", pet_object.get_age())
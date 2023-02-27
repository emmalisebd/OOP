import InsectClass as I

# this is creating an instance of the insect class
mosquito = I.Insect('mosquito', 2, 4)
housefly = I.Insect('housefly', 2, 4)

mosquito.flight_length()
housefly.flight_length()

print(f"the {mosquito.get_name()} can fly up to ")
print(f"the {housefly.get_name()} can fly up to ")

zoo_mass = {
    'lion' : 300,
    'cat'  : 4,
    'dog'  : 15,
    
}
total = 0

for animal in zoo_mass:
    mass = zoo_mass[animal]
    print(animal, mass)
    total += mass
print('Весс всех животных', total)
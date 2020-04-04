
from space.planet import Planet
from space.calc import planet_mass, planet_vol

naboo = Planet('Naboo', 3000, 8, 'Naboo System')

naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)

print(f'{naboo.name} has a mass of {naboo_mass} and a volume of {naboo_vol}')
# class Planet:

#     # class-level attribute, shared by all instances since all planets are round
#     shape = 'round'

#     # instance attribute
#     def __init__(self, name, radius, gravity, system):
#         self.name = name
#         self.radius = radius
#         self.gravity = gravity
#         self.system = system

#     # instance method
#     def orbit(self):  # method cls refers to the class itself
#         return f'{self.name} is orbiting in the {self.system}'

#     # class method
#     @classmethod
#     def commons(cls):
#         return f'All planets are {cls.shape} because of gravity'

#     # method that works on both the class and its instances, method that doesnt take anything in except the parameters passed in explicitely
#     @staticmethod
#     def spin(speed='2000 miles per hour'):  # default value for speed
#         return f'Then planet spins and spins at {speed}'


# # new instance of the class. hoth variable inherits all the properties and methods.
# hoth = Planet('Hoth', 2000, 5.5, 'Hoth System')
# print(f'Name is: {hoth.name}')
# print(f'Radius is: {hoth.radius}')
# print(f'the gravity is: {hoth.gravity}')
# print(hoth.orbit())

# new instance with the same proerty values + its own parameters
# naboo = Planet('Naboo', 3000, 8, 'Naboo System')
# print(f'Name: {naboo.name}')
# print(f'Radius: {naboo.radius}')
# print(naboo.shape)
# print(Planet.shape)
# print(naboo.spin('a very high speed'))
# print(Planet.spin('fast speed'))

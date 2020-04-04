class Planet:

    # class-level attribute, shared by all instances since all planets are round
    shape = 'round'

    # instance attribute
    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    # instance method
    def orbit(self):  # method cls refers to the class itself
        return f'{self.name} is orbiting in the {self.system}'

    # class method
    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'

    # method that works on both the class and its instances, method that doesnt take anything in except the parameters passed in explicitely
    @staticmethod
    def spin(speed='2000 miles per hour'):  # default value for speed
        return f'Then planet spins and spins at {speed}'

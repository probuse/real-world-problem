'''
Credit to Phillip Ahereza
'''
class Car(object):
    def _init_(self, name='General', model='GM', type='Car'):
        self.name = name
        self.model = model
        self.type = type
        self.speed = 0
        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        if self.type != 'trailer':
            self.num_of_wheels = 4
        else:
            self.num_of_wheels = 8
    def is_saloon(self):
        if self.type != 'trailer':
            return True
        else:
            return False
    def drive(self, num):
        """drive car by altering speed
        this method as returns the updated car object.
        """
        if self.type == 'Car':
            self.speed = 10 ** num
        else:
            self.speed = 77
        return self

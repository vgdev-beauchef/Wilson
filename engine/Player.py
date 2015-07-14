import random


def d6(n):
    suma = 0
    for i in range(n):
        suma += random.randint(1, 6)
    return suma


def d6DropLowest(n):
    arr = []
    for i in range(n + 1):
        arr.append(random.randint(1, 6))
    arr = sorted(arr)
    return sum(arr[1:])


class Player(object):
    def __init__(self, name):
        self.name = name
        self.abilities = {
            'STR': 0,
            'DEX': 0,
            'CON': 0,
            'INT': 0,
            'WIS': 0,
            'CHA': 0
        }
        self.position = [10, 10];

    def rollStats(self):
        self.abilities['STR'] = d6(3)
        self.abilities['DEX'] = d6(3)
        self.abilities['CON'] = d6(3)
        self.abilities['INT'] = d6(3)
        self.abilities['WIS'] = d6(3)
        self.abilities['CHA'] = d6(3)

    def rollStatsEasy(self):
        self.abilities['STR'] = d6DropLowest(3)
        self.abilities['DEX'] = d6DropLowest(3)
        self.abilities['CON'] = d6DropLowest(3)
        self.abilities['INT'] = d6DropLowest(3)
        self.abilities['WIS'] = d6DropLowest(3)
        self.abilities['CHA'] = d6DropLowest(3)

    def __str__(self):
        return 'Name: ' + self.name + '\n' + \
               'STR: ' + str(self.abilities['STR']) + '\n' + \
               'DEX: ' + str(self.abilities['DEX']) + '\n' + \
               'CON: ' + str(self.abilities['CON']) + '\n' + \
               'INT: ' + str(self.abilities['INT']) + '\n' + \
               'WIS: ' + str(self.abilities['WIS']) + '\n' + \
               'CHA: ' + str(self.abilities['CHA']) + '\n' + \
               'Mean: ' + str(sum(self.abilities.values()) / 6)


if __name__ == '__main__':
    pl = Player('GengiBro')
    pl.rollStats()
    print(pl)
    pl.rollStatsEasy()
    print(pl)

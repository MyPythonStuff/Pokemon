class Pokemon:
    def __init__(self, name, typ, hp, attack):
        self.name = name
        self.typ = typ
        self.hp = hp
        self.attack = attack

    def retrieve(self):
        print('This pokemon is called ' + self.name + ' and is a ' + self.typ + ' type with ' + str(self.hp)
              + 'hp and an attack of ' + str(self.attack))

    def battle(attack, other):
        other.hp = (other.hp - attack.attack)
        print('target\'s hp is now: ' + other.hp)

    def att(self, other):
        other.hp = (other.hp - self.attack)
        print('target\'s hp is now: ' + str(other.hp))
        #return 'target\'s hp is now: ' + str(other.hp)


pokemon1 = Pokemon('Charmander', 'Fire', 30, 5)
pokemon2 = Pokemon('Squirtle', 'Water', 23, 2)
#print(pokemon1.att(pokemon2))
pokemon1.retrieve()
pokemon2.retrieve()
pokemon1.att(pokemon2)


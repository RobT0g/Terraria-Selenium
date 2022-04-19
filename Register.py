class Weapon:
    def __init__(self, name) -> None:
        self.name = name
    
    def getStats():
        return ('Damage', 'Knockback', 'Use time', 'Rarity', 'Sell')
    
    def insertInfo(self, info):
        for i in info:
            self[i] = info[i]

    def getInfo(self):
        return f'''Nome: {self.name}
        > Damage: {self.damage};
        > Knockback: {self.knockback};
        > Use time: {self.useTime};
        > Velocity: {self.velocity};
        > Rarity: {self.rarity};
        > Sell price: {self.sell}.'''

class WeaponType:
    def __init__(self, name, desc) -> None:
        self.name = name
        self.desc = desc
        self.weapons = {}
    
    def addWeapon(self, weapon):
        self.weapons[weapon.name] = weapon
    

class WeaponClass:
    def __init__(self, name, desc) -> None:
        self.name = name
        self.types = {}
    
    def addType(self, type):
        self.types[type.name] = type

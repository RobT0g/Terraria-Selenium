class Weapon:
    def __init__(self, name) -> None:
        self.name = name
        self.stats = {}
    
    def getStats():
        return ('Damage', 'Knockback', 'Use time', 'Rarity', 'Sell')
    
    def insertInfo(self, info):
        try:
            for i in info:
                self.stats[i] = info[i]
        except Exception as e:
            print(e)
            print(info)

    def getInfo(self):
        info = f'Nome: {self.name}'
        for i in self.stats:
            try:
               info += f'\n>  {i}: {self.stats[i]}'
            except:
                pass
        return info

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

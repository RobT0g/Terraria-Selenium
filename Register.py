import selenium

class Weapon:
    def __init__(self, name, dmg, knock, useTime, vel, rarity, sell) -> None:
        self.name = name
        self.damage = dmg
        self.knockback = knock
        self.useTime = useTime
        self.velocity = vel
        self.rarity = rarity
        self.sell = sell
    
    def getInfo(self):
        return f'''Nome: {self.name}
        > Damage: {self.damage};
        > Knockback: {self.knockback};
        > Use time: {self.useTime};
        > Velocity: {self.velocity};
        > Rarity: {self.rarity};
        > Sell price: {self.sell}.'''
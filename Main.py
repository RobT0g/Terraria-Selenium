from Selector import SelectorOfWeapons

wp = SelectorOfWeapons()
for v in wp.weaponsList:
    print(f'{v.getInfo()}\n')
    print('-'*30)
wp.finish()

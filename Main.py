from Selector import SelectorOfWeapons, SelectorOfTools
from Database import Database

wp = SelectorOfWeapons()
wp.finish()
t = SelectorOfTools()
t.saveOnExcel()
t.finish()
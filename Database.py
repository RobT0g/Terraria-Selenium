import mysql.connector
from Register import Weapon

# cursor.execute(sql) 
# -> Se modifica o banco de dados, é preciso mandar um con.commit() para efetivar as mudanças.
# -> Se lê algum dado, o retorno é feito pelo cursor.fetchall()

class Database:
    def __init__(self) -> None:
        self.con = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'terraria'
        )
        self.cursor = self.con.cursor()

    def uploadSections(self, sectionsList):
        for k, v in enumerate(sectionsList):
            sql = 'insert into sections values '
            for v1 in sectionsList[v]:
                sql += f'''(default, '{v}', '{v1[0]}'), '''
            self.request(sql[:-2] + ';')

    def uploadWeapons(self, weaponsList):
        for k, v in enumerate(weaponsList):
            print(v.stats)
            fields = 'name, '
            stat = f"'{v.name}', "
            for ind, i in enumerate(v.stats):
                stat += f"'{v.stats[i]}', "
                fields += f"{i}, "
            self.request(f"insert into weapons ({fields[:-2]}) values ({stat[:-2]});")
    
    def request(self, sql):
        print(sql) 
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            print(e)
    
db = Database()
w = Weapon('Sword B')
w.insertInfo({'damage': '10'})
db.uploadWeapons([w])
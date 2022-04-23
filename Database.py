import enum
import mysql.connector
from Register import Weapon

# cursor.execute(sql) 
# -> Se modifica o banco de dados, é preciso mandar um con.commit() para efetivar as mudanças.
# -> Se lê algum dado, o retorno é feito pelo cursor.fetchall()

class Database:
    def __init__(self) -> None:
        self.count = 0
        self.con = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'terraria'
        )
        self.cursor = self.con.cursor()
        self.cursor.execute('''delete from weapons where id > '-1';''')
        self.cursor.execute('''delete from sections where id != '0';''')
        self.con.commit()

    def uploadSections(self, sections):
        sql = 'insert into sections values '
        for k, v in enumerate(sections):
            for v1 in sections[v]:
                sql += f'''('{v1[1]}', '{v}', '{v1[0]}'), '''
        self.request(sql[:-2] + ';')

    def uploadWeapons(self, weapons):
        print(weapons)
        print('\n\n\n')
        for k, v in enumerate(weapons):
            sql = 'insert into weapons values '
            if type(weapons[v]) is dict:
                for k1, v1 in enumerate(weapons[v]):
                    for k2, v2 in enumerate(weapons[v][v1]):
                        sql += f'''('{self.count}', '{v}', {self.getWeaponSql(v2)}'{k1}'), '''
                        self.count += 1
            else:
                for k1, v1 in enumerate(weapons[v]):
                    sql += f'''('{self.count}', '{v}', {self.getWeaponSql(v1)}'1'), '''
                    self.count += 1
            self.request(sql[:-2] + ';')
    
    def getWeaponSql(self, weapon):
        sql = ""
        for i in weapon:
            if weapon[i]:
                info = weapon[i].replace("'", '"')
                sql += f"'{info}', "
            else:
                sql += 'default, '
        return sql
    
    def request(self, sql):
        print(sql) 
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            print('ERRO\n', e)
    
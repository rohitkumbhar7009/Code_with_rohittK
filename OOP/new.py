class character :
    def __init__(self,name,health,attack):

        self.name = name
        self.health= health
        self.attack = attack


    def attck_enemy(self):
            print(f'{self.name} attacks with power{self.attack}')

warrior = character("Thor",100,50) 
mage = character('donalf',80,70)

warrior.attck_enemy()
mage.attck_enemy()
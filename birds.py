class Birds:

    def __init__(self, name, size, flying_ability, f_r):
        self.name = name
        self.size = size
        self.flying_ability = flying_ability
        self.f_r = f_r

    def sounding(self):
        print({self.sounding},'поет',)

    def sleeping(self):
        print({self.sleeping},'спит',)

    def eating(self):
        print({self.eating},'ест',)

    def f_aTOf_r(self):
        if self.flying_ability == 'да':
            print ('птичка летны и летит',  self.f_r)
        else:
            print ('птичка нелетны')



bird = Birds('ilyha', 22, 'да', 30)

print (bird.size)
print (bird.name)
print (bird.flying_ability)



bird.sounding()
bird.eating()
bird.sleeping()

bird.f_aTOf_r()

orel = Birds('орел', 22, 'нет', 30)

print (orel.size)
print (orel.name)
print (orel.flying_ability)



orel.sounding()
orel.eating()
orel.sleeping()

orel.f_aTOf_r()
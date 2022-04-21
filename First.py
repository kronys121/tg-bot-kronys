from pprint import pprint


class Purse:
    def __init__(self,valuta,name='Unknown'):
        self.money = 0
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, howmany):
        self.money = self.money + howmany

    def top_down_balance(self,howmany):
        if self.money - howmany < 0:

            print('Нету денег')
            raise ValueError ('Нету денег')
        self.money = self.money - howmany
    
    def convector_usd(self,usd):
        self.money = self.money * usd

    def convector_eur(self,eur):
        self.money = self.money * eur


    def info(self):
        return self.money

 
x = Purse('USD')
y = Purse("EUR",'Bill')
x.top_up_balance(100)
print(x.money)
x.convector_eur(73)
print('EUR', x.money)




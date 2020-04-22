

class predmet:
    pass


class live(predmet):
    pass


class unlive(predmet):
    pass


class trotuar(unlive):
    pass


class tvarini(live):
    def dichati(self):
        print('дышит')

    def ruchatic(self):
        print('двигается')

    def harchudatic_ijeu(self):
        print('ест еду')


class ssavci(tvarini):
    def goduvati_ditinu_molokom(self):
        print('кормит детеныша')


class jiraf(ssavci):
    def isti_listja(self):
        print('ест листву')

    def dance(self):
        print('Левая нога вперед')
        print('Левая нога назад')
        print('Правая нога вперед')
        print('Правая нога назад')

    def shukati_iju(self):
        print('искать еду')
        self.ruchatic()
        print('Я нашол еду')
        self.harchudatic_ijeu()

    def isti_listja_z_dereva(self):
        self.harchudatic_ijeu()

    def tancuvatu(self):
        self.dance()
        self.ruchatic()
        self.dance()
        self.ruchatic()

    def __init__(self, plama):
        self.jiraf_plama = plama


redji = jiraf(80)
garold = jiraf(90)

redji.isti_listja()
garold.tancuvatu()

ocvald = jiraf(100)
gertruda = jiraf(150)

print(ocvald.jiraf_plama)


print(gertruda.tancuvatu())


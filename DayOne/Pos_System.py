class Menu:
    menu=[]
    # we only sell Americanos and Bagels
    Americanos = "Americanos"
    Bagels = "Bagels"

    def __init__(self,americanos,bagels ):
        self.Americanos=americanos
        self.Bagels=bagels
        self.menu=[]

    def mutiple(self,americanos,bagels):
        print(americanos, bagels)

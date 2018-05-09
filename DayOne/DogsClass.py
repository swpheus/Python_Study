class Dogs :
    dogs=[]
    def __init__(self,name,weight,breed):
        self.name = name
        self.weight =weight
        self.breed = breed
        self.tricks =[]
    def learntrick(self,trick):
        self.tricks.append(trick)


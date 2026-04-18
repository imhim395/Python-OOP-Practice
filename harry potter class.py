class harrypotter_but_cats:#idk why ts ass name
    def __init__(self, input_name, input_breed, input_age, input_tuffness, isgoodguy):
        self.name = input_name
        self.breed = input_breed
        self.age = input_age
        self.tuffness = input_tuffness
        self.isgoodguy = isgoodguy
    def cat_aura_celebration(self):
        if self.age in range (1, 5):#any car in ages 1-4
            print(f"ts cat", self.name, "has aura")
        else:
            print(self.name,"status = unc")
    def goodguyorbadguy(self):
        if self.isgoodguy:
            print(self.name,"is a good guy")
        else:
            print(self.name, "is a bad guy")

catone = harrypotter_but_cats("harry potter", "british shorthair(whatever tf ts is", 2, True, True)#name is albus to tuff so hes got to be tuff
cattwo = harrypotter_but_cats("albus dumbledore", "ragdoll", 5, False, True)#cause ts cat is unc
catthree = harrypotter_but_cats("lord voldemort", "black cat", 4, False, False)#subjective tuffness

catone.cat_aura_celebration()
cattwo.cat_aura_celebration()
catthree.cat_aura_celebration()

catone.goodguyorbadguy()
cattwo.goodguyorbadguy()
catthree.goodguyorbadguy()
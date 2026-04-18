class harrypotter_but_cats:#idk why ts ass name
    def __init__(self, input_name, input_breed, input_age, input_tuffness):
        self.name = input_name
        self.breed = input_breed
        self.age = input_age
        self.tuffness = input_tuffness
    def cat_aura_celebration(self):
        if self.age in range (3, 5):#any car in ages 3-4
            print(f"ts cat", self.name, "has aura")
        else:
            print(self.name,"status = unc")

catone = harrypotter_but_cats("harry potter", "british shorthair(whatever tf ts is", 3, True)#name is albus to tuff so hes got to be tuff
cattwo = harrypotter_but_cats("albus dumbledore", "ragdoll", 5, False)#cause ts cat is unc

catone.cat_aura_celebration()
cattwo.cat_aura_celebration()
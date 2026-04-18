class Dog:
    def __init__(self, input_name, input_breed, input_age, input_friendliness):
        self.name = input_name
        self.breed = input_breed
        self.age = input_age
        self.is_friendly = input_friendliness

    def bday(self):
        print(f"today, it is {self.name}'s birthday!")#f-string to make the shi cleaner

    def bark(self):
        if self.is_friendly is False:
            print(self.name,"is barking at you, arf arf")#bruh
        else:
            print(self.name, "is friendly and wants to play with you")


dog_one = Dog("pierre", "golden retriever", "5", True)
dog_two = Dog("sparky", "black lab", "7", False)

dog_one.bday()
dog_two.bday()
dog_one.bark()
dog_two.bark()
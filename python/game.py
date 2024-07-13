import random 
class pokemon: # parent
    
    def __init__(self,name,health,element):
        self.name = name
        self.health = health
        self.element = element

    def doMove(self):
        print("Pokemon Move")

    def doEat(self):
        print("Pokemon Eat")

    def __str__(self):
        return f"Name: {self.name} \nHealth: {self.health} \nElement: {self.element}"

class Jigglypuff(pokemon): # child

    def __init__(self, name, health, element, lungcapacity):
        super().__init__(name, health, element)
        self.lungcapacity = lungcapacity
    
    def doMove(self): # override is where we create method in child that has in parent
        super().doMove()
        print("Jigglypuff can float")

    def __str__(self):
        return f"Name: {self.name}\nHealth: {self.health}\nElement: {self.element}\nLungcapacity: {self.lungcapacity}"


class Pikachu(pokemon):

    def __init__(self, name, health, element, electricity):
        super().__init__(name, health, element)
        self.electricity = electricity

#pokemon = jigglypuff("j1", 75, "Fairy", 92 )
#pokemon.doMove()
    def __str__(self):
        return f"Name: {self.name}\nHealth: {self.health}\nElement: {self.element}\nElectricity: {self.electricity}"

class Game:
    
    def __init__(self):

        self.element = ["thunder", "fire", "ghost","ice"]
        self.pokemon ={
            "jigglypuff":[Jigglypuff(f"J{i}", random.randint(50, 100), self.element[random.randint(0, len(self.element) - 1)], random.randint(50, 100)) for i in range(0, random.randint(3, 15))],
            "pikachu":[Pikachu(f"P{i}", random.randint(50, 100), self.element[random.randint(0, len(self.element) - 1)], random.randint(50, 100)) for i in range(0, random.randint(5, 20))]
        }
    def __str__(self):
        message = ""
        for pokemonname, pokemonlist in self.pokemon.items():
            for pokemon in pokemonlist:
                message = message + pokemon.__str__() + "\n" + ("-" * 20) + "\n"            
                return message
game = Game()
print(game)

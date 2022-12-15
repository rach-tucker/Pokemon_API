import requests

class Pokemon:
    base_url = 'https://pokeapi.co/api/v2/pokemon'

    def __init__(self, name):
        self.name = name 
        
    def get(self, name):
        request_url = f"{self.base_url}/{name}"
        pokemon_response = requests.get(request_url)
        if pokemon_response.ok:
            return pokemon_response.json()
        else: 
            print('There was an error')
        
        
    def get_height_weight(self, name):
        poke_data = self.get(name)
        poke_name = poke_data['name']
        poke_height = poke_data['height']
        poke_weight = poke_data['weight']
        poke_height_weight = Pokeheightweight(poke_name, poke_height, poke_weight)
        return poke_height_weight
        
class Pokeheightweight:
    
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        
    def __str__(self):
        return f"{self.name} has a height of {self.height} and a weight of {self.weight}."
    
my_poke = Pokemon('pikachu')
print(my_poke.get_height_weight('pikachu'))

        
    
from random import randint
import requests
class Pokemon:
    pokemons = {}
    def __init__(self, pokemon_trainer): 
        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        
        # Add type attribute
        self.type = self.get_type()  

        self.img = self.get_img()
        self.name = self.get_name()
        Pokemon.pokemons[pokemon_trainer] = self
    def get_type(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['types'][0]['type']['name']
        else:
            return "Normal" 


    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()  
            return data['sprites']['other']['home']['front_default']
        else:
            return None

    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    def info(self):
        return f"Имя твоего покемона: {self.name}, Тип покемона: {self.type}"
    def show_img(self):
        return self.img

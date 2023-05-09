#query to return all pokemon named "Pikachu"
from pymongo import MongoClient

client = MongoClient()
db = client.pokemon
pokemons = db.pokemon_data.find({"name": "Pikachu"})

for pokemon in pokemons:
    print(pokemon)

#Query to return all Pokemon with an attack greater than 150
from pymongo import MongoClient

client = MongoClient()
db = client.pokemon
pokemons = db.pokemon_data.find({"attack": {"$gt": 150}})

for pokemon in pokemons:
    print(pokemon)

#Query to return all Pokemon with an ability of "Overgrow"
from pymongo import MongoClient

client = MongoClient()
db = client.pokemon
pokemons = db.pokemon_data.find({"abilities": "Overgrow"})

for pokemon in pokemons:
    print(pokemon)

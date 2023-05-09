import sqlite3
from pymongo import MongoClient
connection = sqlite3.connect("pokemon.sqlite")
con = connection.cursor()

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

pikachu = pokemonColl.find_one({"name": "Pikachu"})

def some_function(pokemonid):
   return pokemonColl.find_one({"pokedex_number":pokemonid})


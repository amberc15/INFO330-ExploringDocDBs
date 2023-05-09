import sqlite3 
from pymongo import MongoClient
connection = sqlite3.connect("pokemon.sqlite")
con = connection.cursor()

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

getName = con.execute("SELECT name FROM pokemon").fetchone()
getNumber = con.execute("SELECT pokedex_number FROM pokemon").fetchone()
firstType = con.execute("SELECT type1 FROM pokemon_types_view").fetchone()
secondType = con.execute("SELECT type2 FROM pokemon_types_view").fetchone()
getHp = con.execute("SELECT hp FROM pokemon").fetchone()
getAttack = con.execute("SELECT attack from pokemon").fetchone()
getDefense = con.execute("SELECT defense from pokemon").fetchone()
getSpeed = con.execute("SELECT speed from pokemon").fetchone()
sp_attack = con.execute("SELECT sp_attack from pokemon").fetchone()
sp_defense = con.execute("SELECT sp_defense from pokemon").fetchone()
newList = [getName, getNumber, firstType, secondType, getHp, getAttack, getDefense, getSpeed, sp_attack, sp_defense]
newTable = con.execute("JOIN pokemon_types_view type1 ON pokemon.name = type1.name JOIN pokemon_abilities ON pokemon.id = pokemon_abilities.pokemon_id JOIN ability ON pokemon.ability_id = ability.id").fetchone()

pokemon = {
       "name": newList[0],
       "pokedex_number": newList[1],
       "types": [newList[2], newList[3]],
       "hp": newList[4],
       "attack": newList[5],
       "defense": newList[6],
       "speed": newList[7],
       "sp_attack": newList[8],
       "sp_defense": newList[9]
       #"abilities": abilities
   }
pokemonColl.insert_one(pokemon)

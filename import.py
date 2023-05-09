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

for i in range(1, 802):
    rows = con.execute("SELECT * FROM pokemon WHERE id = " + str(i)).fetchone()
    typeOne = con.execute("SELECT * FROM type AS T LEFT OUTER JOIN pokemon_type AS PT ON T.id = PT.type_id WHERE pokemon_id = " 
                         + str(i) + " AND which = 2").fetchone() 
    typeTwo = con.execute("SELECT * FROM type AS T LEFT OUTER JOIN pokemon_type AS PT ON T.id = PT.type_id WHERE pokemon_id = "
                         + str(i) + " AND which = 2").fetchone()
    abilities = con.execute("SELECT * FROM ability AS A LEFT OUTER JOIN pokemon_abilities AS PA on A.id = PA.ability_id WHERE pokemon_id = "
                         + str(i)).fetchmany(6)
    newAbilities = []

pokemon = {
       "name": str(newList[0]),
       "pokedex_number": str(newList[1]),
       "types": str([newList[2], newList[3]]),
       "hp": str(newList[4]),
       "attack": str(newList[5]),
       "defense": str(newList[6]),
       "speed": str(newList[7]),
       "sp_attack": str(newList[8]),
       "sp_defense": str(newList[9]),
       "abilities": str(abilities)
}
pokemonColl.insert_one(pokemon)

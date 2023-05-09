from pymongo import MongoClient
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

pikachuQuery = pokemonColl.find_one({"name": "Pikachu"})
for i, value in (pikachuQuery):
    print(pikachuQuery)

attack = {"attack": {"$gt": 150}}
outcome = pokemonColl.find(attack)
print("Pokemon with attack greater than 150: ")
for i,value in (attack):
    print(outcome)

overgrow = {'abilities': 'Overgrow'}
pokemon_overgrow = pokemonColl.find(overgrow)
for i, value in (pokemon_overgrow):
    print(pokemon_overgrow)


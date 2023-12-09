import requests


response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
              json={
    "name": "Biba",
    "photo": "https://dolnikov.ru/pokemons/albums/012.png"
    }, 
    headers= {'Content-Type': 'application/json',
             'trainer_token': '0294501b3a165ef18729af9b95429860'}
           )
print(response)

response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons', 
              json={
    "pokemon_id": "21485",
    "name": "Listovik10",
    "photo": "https://dolnikov.ru/pokemons/albums/011.png"
    }, 
    headers= {'Content-Type': 'application/json',
             'trainer_token': '0294501b3a165ef18729af9b95429860'}
           )
print(response)

response = requests.post(url='https://api.pokemonbattle.me:9104//trainers/add_pokeball', 
              json={
    "pokemon_id": "21485",
   }, 
    headers= {'Content-Type': 'application/json',
             'trainer_token': '0294501b3a165ef18729af9b95429860'}
           )
print(response)

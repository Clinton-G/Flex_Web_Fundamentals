import requests

def fetch_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(pokemon_name, "Failed")
        return None

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
        total_weight += pokemon['weight']
    
    if len(pokemon_list) > 0:
        return total_weight / len(pokemon_list)
    else:
        return 0

def main():
    pokemon_names = ["pikachu", "bulbasaur", "charmander"]
    pokemon_data_list = []
    
    for name in pokemon_names:
        pokemon_data = fetch_pokemon_data(name)
        if pokemon_data:
            pokemon_data_list.append({
                'name': pokemon_data['name'],
                'abilities': [ability['ability']['name'] for ability in pokemon_data['abilities']],
                'weight': pokemon_data['weight']
            })
    
    average_weight = calculate_average_weight(pokemon_data_list)
    
    for pokemon in pokemon_data_list:
        print("Name:", pokemon['name'])
        print("Abilities:")
        for ability in pokemon['abilities']:
            print(ability)
        print("Weight:", pokemon['weight'])
        print()

    print("\nAverage Weight:", average_weight)

if __name__ == "__main__":
    main()

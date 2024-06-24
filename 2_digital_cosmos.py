import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    
    if response.status_code == 200:
        planets_data = response.json()['bodies']
        return planets_data
    else:
        print(f"Failed")
        return []

def find_heaviest_planet(planets):
    heaviest_planet = None
    max_mass = 0
    
    for planet in planets:
        if planet['isPlanet'] and 'mass' in planet:
            mass_value = planet['mass']['massValue']
            if mass_value > max_mass:
                max_mass = mass_value
                heaviest_planet = planet
    
    if heaviest_planet:
        return heaviest_planet['englishName'], heaviest_planet['mass']['massValue']
    else:
        return None, None

def find_longest_orbit_period_planet(planets):
    longest_orbit_planet = None
    max_orbit_period = 0
    
    for planet in planets:
        if planet['isPlanet'] and 'sideralOrbit' in planet:
            orbit_period = planet['sideralOrbit']
            if orbit_period > max_orbit_period:
                max_orbit_period = orbit_period
                longest_orbit_planet = planet
    
    if longest_orbit_planet:
        return longest_orbit_planet['englishName'], longest_orbit_planet['sideralOrbit']
    else:
        return None, None

if __name__ == "__main__":
    planets = fetch_planet_data()
    
    heaviest_name, heaviest_mass = find_heaviest_planet(planets)
    if heaviest_name and heaviest_mass:
        print(f"The heaviest planet is {heaviest_name} with a mass of {heaviest_mass} kg.")
    else:
        print("Heaviest Failed")
    
    longest_orbit_name, longest_orbit_period = find_longest_orbit_period_planet(planets)
    if longest_orbit_name and longest_orbit_period:
        print(f"The planet with the longest orbit period is {longest_orbit_name} with an orbit period of {longest_orbit_period} days.")
    else:
        print("Longest Orbit Failed")

import json

species_file = open('species_data.json')

species_data = json.load(species_file)

print(len(species_data))

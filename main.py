import csv
import json
from operator import truediv

species_file = open('data/cnddb_data.json')
species_data = json.load(species_file)

results_data = []

with open('data/herps.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        for species in species_data:
            if row[0].strip().lower() in species["Scientific Name"].lower():
                results_data.append(species)
                print(species)


with open("data/endangered_herp_list.json", "w") as outfile:
    json.dump(results_data, outfile)

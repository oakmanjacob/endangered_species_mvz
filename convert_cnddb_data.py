import csv
import json

species_list = [];
counter = 0;

with open('cnddb_data.csv') as csvfile:
    reader = reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        species = {
            "Scientific Name":row[0].replace("\n", " "),
            "Common Name":row[1].replace("\n", " "),
            "Comments":row[2].replace("\n", " "),
            "Global Rank":row[3].replace("\n", " "),
            "State Rank":row[4].replace("\n", " "),
            "ESA":row[5].replace("\n", " "),
            "CESA":row[6].replace("\n", " "),
            "Other Status":row[7].replace("\n", " "),
            "Records in CNDDB?":row[8].replace("\n", " "),
            "End Notes?":row[9].replace("\n", " "),

        }
        
        if species["Scientific Name"] != "Scientific Name":
            species_list.append(species)


with open("cnddb_data.json", "w") as outfile:
    json.dump(species_list, outfile)
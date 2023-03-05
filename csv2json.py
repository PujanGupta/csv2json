import csv
import json

def csv2json(csvFile,jsonFile):
    #read csv
    with open(csvFile, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    #write json
    with open(jsonFile, 'w') as json_file:
        json.dump(data, json_file, indent=4)

import csv
cereals_filename = 'cereal_grains.csv'

with open(cereals_filename, encoding='utf-8', newline='') as cereal_file:
    reader = csv.DictReader(cereal_file)
    for row in reader:
        print(row)
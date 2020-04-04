import csv

with open("emails.csv", "r") as file:
    reader = csv.DictReader(file)
    records = []
    for row in reader:
        records.append(dict(row))

for i in records:
    print(i["email"])

import csv
groceries = []
with open('csvs/shopping.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        groceries.append(row)

#print(groceries)

#print(groceries[2]['name'])


tony = {'name': 'tony', 'nutritious': 'False', 'id': '5'}

groceries.append(tony)

with open('csvs/updated_groceries.csv', 'w', newline = "") as fout:
    column_names = ['id', 'name', 'nutritious']
    dictwriter = csv.DictWriter(fout, fieldnames=column_names)
    dictwriter.writeheader()
    for row in groceries:
        dictwriter.writerow(row)

for item in groceries:
    print(item["name"])

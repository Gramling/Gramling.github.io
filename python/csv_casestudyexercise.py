import csv
#with open('csvs/ripper.csv', 'r') as csvfile:
#    our_reader = csv.reader(csvfile)
#    names = [row for row in our_reader]

#print(names[0])

#all_texts = []
#with open('csvs/ripper.csv', 'r') as csvfile:
#    reader = csv.reader(csvfile)
#    for row in reader:
#        all_texts.append(row)

#print(all_texts[2])

#with open('csvs/ripper.csv', 'r') as csvfile:
#    our_reader = csv.reader(csvfile)
#    all_texts = [row[4] for row in our_reader]

#print(all_texts[0])

#with open('csvs/ripper.csv', 'r') as csvfile:
#    our_reader = csv.reader(csvfile)
#    results = [row for row in our_reader]

#dates = [row[3] for row in results]
#print(min(dates))
#print(max(dates))

new_file = []
with open('csvs/ripper.csv', 'r') as csvfile:
    our_reader = csv.reader(csvfile)
    for row in our_reader:
        new_file.append(row)

for row in new_file:
    row[4] = row[4].lower()

print(new_file[0])

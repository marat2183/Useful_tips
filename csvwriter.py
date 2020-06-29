import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldsname = ['name', 'surname']
    writer = csv.DictWriter(csvfile, fieldnames=fieldsname)
    writer.writeheader()
    writer.writerow({'name':'Marat', 'su'
                                     'rname': 'Grigoryan'})
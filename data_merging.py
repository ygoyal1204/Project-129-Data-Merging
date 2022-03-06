import csv

dataset1 = []
dataset2 = []

with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    
    for row in csvreader:
        dataset1.append(row)

with open("unit_coverted_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    
    for row in csvreader:
        dataset2.append(row)

headers1 = dataset1[0]
stardata1 = dataset1[1:]

headers2 = dataset2[0]
stardata2 = dataset2[1:]

headers = headers1 
stardata = []

for i in stardata1:
    stardata.append(i)

for j in stardata2:
    stardata.append(j)

with open("final.csv", 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stardata)
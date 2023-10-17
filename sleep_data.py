import csv

with open("oura_2021-11-04_2022-01-04_trends.csv") as file:
    reader = csv.reader(file, delimiter = ",")
    for line in file:
        print(line)
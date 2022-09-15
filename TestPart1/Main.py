import csv

with open('test_data - Copy.csv', 'r', encoding="utf8") as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        print(row)
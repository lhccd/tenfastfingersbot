import csv

with open('/Users/lorenz/PycharmProjects/TenFastfingersBot/linklist_inserate.txt') as csvfile:
    readCSV = csv.reader(csvfile)
    linklist = []
    for row in readCSV:
        linklist.append(row[0])

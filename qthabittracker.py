import csv

file = open("Habits-Tracker.csv", "w")
writer = csv.writer(file)

stop = False
while True:
    data = [input("NAME: "), (input("AGE: "))]
    writer.writerow(data)

    breaker = input("Keep going? y/n: ")
    if breaker == "n":
        break

file.close()
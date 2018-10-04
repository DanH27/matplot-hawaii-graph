import matplotlib.pyplot as plt
import numpy as np
import csv

results = []
counties = []
populations = []

with open("HawaiiStats.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    next(reader, None)

    for row in reader:
        counties.append(row[0])
        populations.append(int(row[1]))

plt.bar(counties, populations)
plt.show()

import statistics
from statistics import mean, median, mode


print(statistics.mean([100,90,101,102,109,102]), "This value1:")
print(statistics.mean(range(10)), "This is value2:")
print(statistics.median(range(10)), " This is value3:")

sc = statistics.median(range(999))
print(sc)


print(mean(range(99)))
print(mode(range(99)))
print(median(range(99)))
names = []

with open("names.txt") as f:
    for line in f:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")
print("Not sorted below")

for name in names:
    print(f"Hello, {name}")


# all above done in more pythonic way
with open("names.txt") as f2:
    for line in sorted(f2):
        print("Hello this is directly sorted in open::",line.rstrip())

for name in sorted(names, reverse=True):
    print(f"Hello reversed alphabetically:>, {name}")
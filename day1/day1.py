
f = open("input.txt", "r")

maxCalories = -100

currentCalories = 0
for line in f:
    if line.isspace():
        if currentCalories > maxCalories:
            maxCalories = currentCalories
        currentCalories = 0
    else:
        currentCalories += int(line)

print(maxCalories)

fruits = ["Apple", "Tomato", "Banana", "Orange", "Lemon"]
print(fruits)

for i in range(len(fruits) - 1, -1, -1):
    if fruits[i] == "Banana":
        fruits.pop(i)
    
print(fruits)
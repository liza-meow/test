n= int(input("Введите n: "))
m = int(input("Введите m: "))
circle_array = [i for i in range(1, n+1)]
path = []

for i in range(m, n+1, m):
path.append(circle_array[i % n])

print("Путь:", path)
import sys


def read_coordinates(file_path):
    with open(file_path, 'r') as file:
        coordinates = []
        for line in file:
            x, y = map(int, line.split())
            coordinates.append((x, y))
    return coordinates


def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def check_point_position(center_x, center_y, radius, point_x, point_y):
    distance = calculate_distance(center_x, center_y, point_x, point_y)
    if distance == radius:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(
            "Неверное количество аргументов. Укажите путь к файлу с координатами окружности и радиусом, а затем к файлу с координатами точек.")
    else:
        center_x, center_y, radius = map(int, read_coordinates(sys.argv[1])[0])
        points = read_coordinates(sys.argv[2])

        for point in points:
            position = check_point_position(center_x, center_y, radius, point[0], point[1])
            print(position)
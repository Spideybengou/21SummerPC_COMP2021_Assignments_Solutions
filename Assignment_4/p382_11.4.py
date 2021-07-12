workHours = [
    [2, 4, 3, 4, 5, 8, 8],
    [7, 3, 4, 3, 3, 4, 4],
    [3, 3, 4, 3, 3, 2, 2],
    [9, 3, 4, 7, 3, 4, 1],
    [3, 5, 4, 3, 6, 3, 8],
    [3, 4, 4, 6, 3, 4, 4],
    [3, 7, 4, 8, 3, 8, 4],
    [6, 3, 5, 9, 2, 7, 9]]

matrix = []

for row in range(len(workHours)):
    totalHours = sum(workHours[row])
    matrix.append([totalHours, "Employee " + str(row)])

matrix.sort(reverse=True)

for i in matrix:
    print(i[1]+"'s total hours =", i[0])

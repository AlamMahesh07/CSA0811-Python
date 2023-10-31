def digits_sum():
    for i in reversed(range(len(triangle_num) - 1)):
        for j in range(len(triangle_num[i])):
            triangle_num[i][j] += max(triangle_num[i + 1][j],
triangle_num[i + 1][j + 1])
            return str(triangle_num[0][0])
triangle_num =[[3],[4,6],[2,7,6],[8,5,9,3]]
print(digits_sum())

a = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
rows = len(a);
cols = len(a[0]);
for i in range(0, rows):
    sumRow = 0;
for j in range(0, cols):
    sumRow = sumRow + a[i][j];
print("Sum of " + str(i+1) +" row: " + str(sumRow));
for i in range(0, rows):
    sumCol = 0;
for j in range(0, cols):
    sumCol = sumCol + a[j][i];
print("Sum of " + str(i+1) +" column: " + str(sumCol));
diagonal=0
for k in range(0,rows):
    diagonal=diagonal+a[k][k]
print("Diagonal sum",diagonal)

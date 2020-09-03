#OTHELLO
matrix = []
for i in range(8):
  a = list(input())
  matrix.append(a)

s = input()
la = input()
m = input()
lb = input()
q = input()

if s == 'W':
  p = 'B'
else:
  p = 'W'
  
k = list(m)
m = int(k[1])
n = int(k[2])

temp = 0

if la == 'l':
  for i in range(8):
    for j in range(8):
      if matrix[i][j] == p:
        if i <= 0 or i >= 7 or j <= 0 or j >= 7:
          print("No Legal Move")
          temp = 1
          break
        if matrix[i-1][j] == s and matrix[i+1][j] == '-':
          li = [i+1+1, j+1]
          print(tuple(li))
        if matrix[i+1][j] == s and matrix[i-1][j] == '-':
          li = [i-1+1, j+1]
          print(tuple(li))
        if matrix[i][j+1] == s and matrix[i][j-1] == '-':
          li = [i+1, j-1+1]
          print(tuple(li))
        if matrix[i][j-1] == s and matrix[i][j+1] == '-':
          li = [i+1, j+1+1]
          print(tuple(li))
        if matrix[i-1][j-1] == s and matrix[i+1][j+1] == '-':
          li = [i+1+1, j+1+1]
          print(tuple(li))
        if matrix[i+1][j+1] == s and matrix[i-1][j-1] == '-':
          li = [i, j]
          print(tuple(li))
        if matrix[i-1][j+1] == s and matrix[i+1][j-1] == '-':
          li = [i+1+1, j]
          print(tuple(li))
        if matrix[i+1][j-1] == s and matrix[i-1][j+1] == '-':
          li = [i, j+1+1]
          print(tuple(li))
    if temp == 1:
      break
      
             
if temp == 1:
  s, p = p, s
  
matrix[m-1][n-1] = s
for i in range(8):
  for j in range(8):
    if matrix[m][n-1] == p and matrix[m+1][n-1] == s:
      matrix[m][n-1] = s
    if matrix[m-2][n-1] == p and matrix[m-3][n-1] == s:
      matrix[m-2][n-1] = s
    if matrix[m-1][n] == p and matrix[m-1][n+1] == s:
      matrix[m-1][n] = s
    if matrix[m-1][n-2] == p and matrix[m-1][n-3] == s:
      matrix[m-1][n-2] = s
    if matrix[m-2][n-2] == p and matrix[m-3][n-3] == s:
      matrix[m-2][n-2] = s
    if matrix[m-2][n] == p and matrix[m-3][n+1] == s:
      matrix[m-2][n] = s
    if matrix[m][n-2] == p and matrix[m+1][n-3] == s:
      matrix[m][n-2] = s
    if matrix[m][n] == p and matrix[m+1][n+1] == s:
      matrix[m][n] = s

        
r = 0
c = 0
for i in range(8):
  for j in range(8):
    if matrix[i][j] == 'W':
      c += 1
    elif matrix[i][j] == 'B':
      r += 1
print('Black :',r, 'White :',c)
  
if lb == 'l':
  for i in range(8):
    for j in range(8):
      if matrix[i][j] == s:
        if j == 0:
          continue
        if matrix[i-1][j] == p:
          if matrix[i+1][j] != p and matrix[i+1][j] == '-':
            li = [i+1+1, j+1]
            print(tuple(li))
        if matrix[i+1][j] == p:
          if matrix[i-1][j] != p and matrix[i-1][j] == '-':
            li = [i-1+1, j+1]
            print(tuple(li))
        if matrix[i][j+1] == p:
          if matrix[i][j-1] != p and matrix[i][j-1] == '-':
            li = [i+1, j-1+1]
            print(tuple(li))
        if matrix[i][j-1] == p:
          if matrix[i][j+1] != p and matrix[i][j+1] == '-':
            li = [i+1, j+1+1]
            print(tuple(li))
        if matrix[i-1][j-1] == p:
          if matrix[i+1][j+1] != p and matrix[i+1][j+1] == '-':
            li = [i+1+1, j+1+1]
            print(tuple(li))
        if matrix[i+1][j+1] == p:
          if matrix[i-1][j-1] != p and matrix[i-1][j-1] == '-':
            li = [i, j]
            print(tuple(li))
        if matrix[i-1][j+1] == p:
          if matrix[i+1][j-1] != p and matrix[i+1][j-1] == '-':
            li = [i+1+1, j]
            print(tuple(li))
        if matrix[i+1][j-1] == p:
          if matrix[i-1][j+1] != p and matrix[i-1][j+1] == '-':
            li = [i, j+1+1]
            print(tuple(li))
        
  
for i in matrix:
  for j in i:
    print(j,end = ' ')
  print()
#@Author : Sudip Mitra
for i in range(int(input())):
  n = list(map(int, input().split()))
  n.sort()
  print(n[-2])

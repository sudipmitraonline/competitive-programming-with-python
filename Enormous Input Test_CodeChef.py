#@Author : Sudip Mitra
n, k = map(int, input().split())
count = 0
word = []
for i in range(n):
  num = int(input())
  word.append(num)

  if word[i] % k == 0:
    count += 1
print(count)

n = int(input())
l = []
for m in ("SHCD"):
  for i in range(1, 14):
    l.append(m+" "+str(i))
for i in range(n):
  s = input()
  l.remove(s)
for ele in l:
  print(ele)
def dfs(i, j):
  if a[i][j] == ".":
    a[i][j] = "#"

  res=1
  wc=0
  bc=0

  for dy in range(-1, 2):
    for dx in range(-1, 2):
      if (dx==0 and dy!=0) or (dx!=0 and dy==0):
        pass
      else:
        continue
      
      ny = i+dy
      nx = j+dx

      if 0<=nx<=w-1 and 0<=ny<=h-1 and a[ny][nx]!="#":
        if a[ny][nx] == ".":
          wct, bct, rest = dfs(ny, nx)
          wc+=wct
          bc+=bct
          res+=rest
        elif a[ny][nx]=="W":
          wc+=1
        elif a[ny][nx]=="B":
          bc+=1
          
  return wc, bc, res

import sys
sys.setrecursionlimit(100000)

while True:
  w, h = map(int, input().split())
  wans = 0
  bans = 0
  if w==0 and h==0:
    break
  a = [list(input()) for _ in range(h)]

  for i in range(w):
    for j in range(h):
      if a[j][i] ==".":
        wc, bc, res = dfs(j, i)
        if wc>0 and bc==0:
          wans+=res
        elif wc==0 and bc>0:
          bans+=res
  print(bans, wans)

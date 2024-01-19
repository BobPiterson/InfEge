import sys
#m = (88, 90, 91, 92, 93, 100, 95, 89, 87, 77, 76, 61, 60, 49, 45, 40, 12, 9, 3, 6, 8, 11, 19, 24, 33, 65, 67, 70, 73, 82)
#m = (100, 95, 89, 87, 77, 76, 61, 60, 49, 45, 40, 12, 9, 3)
# m = (100, 95, 89, 87, 77, 76, 61, 60, 49, 45, 40, 12, 9, 3, 6, 8, 11, 19, 24, 33, 65, 67, 70, 73, 82)
# m = (88, 90, 91, 92, 93, 100, 95, 89, 87, 77, 76, 61, 60, 49, 45, 40, 12, 9, 3)
# m  = (6, 9, 8, 5, 3, 1, 2)

class MyList():
   def __init__(self, length):
      self.requests = 0
      # self.indexes = {i + 1: v for i, v in enumerate(m)}
      self.indexes = dict()
      self.length = length

   def __getitem__(self, idx):
      self.requests += 1
      idx += 1
      val = self.indexes.get(idx, 0)
      if val:
         return val

      sys.stdout.write(f'{idx}\n')
      sys.stdout.flush()
      val = int(input())
      self.indexes[idx] = val
      return val
    
   def __len__(self):
      return self.length


# find = [95, 45, 65]
# n, k = len(m), len(find)

n, k = map(int, input().split())
find = map(int, input().split())


m = MyList(n)

#print (m)
#print(len(m))

if len(m) < 500:
   
   for i in range(0, len(m)):
       m[i]

   sys.stdout.write(f'0\n')
   sys.stdout.flush()
   exit()


l = 0
r = len(m) - 1
list_ekstremum_up = set()
list_ekstremum_down = set()

# Часть 1. Поиск экстремумов

def func_ect_left (l, r): 
   #print ('----------------------------')
   #print(l, r)
   if l + 1 == r:
       return l, r
   direct_l = (m[l+1] > m[l])
   #print(direct_l)
   direct_r = (m[r] > m[r-1])
   #print (direct_r)
   
   if (direct_l == direct_r):
       Stable = True
   else:
       Stable = False
    
   if not Stable:
      direct_l = (m[l+1] > m[l])
      direct_r = (m[(r+l) // 2] > m[(r+l) // 2 - 1])
      if (direct_l == direct_r):
         l = (r+l) // 2
      else: 
         r = (r+l) // 2
   else:
      r = (r+l) // 2 
        
   #print(l, r)
   #time.sleep(0.5)
   return func_ect_left (l, r)
       

q, tmp = func_ect_left(l, r)
#print('Найден первый экстремум', q)


def func_ect_right (l, r): 
   #print ('----------------------------')
   #print(l, r)
   if l + 1 == r:
       return l, r
   direct_l = (m[l+1] > m[l])
   #print(direct_l)
   direct_r = (m[r] > m[r-1])
   #print (direct_r)
   
   if (direct_l == direct_r):
       Stable = True
   else:
       Stable = False
    
   if not Stable:
      direct_l = (m[(r+l) // 2 + 1] > m[(r+l) // 2])
      direct_r = (m[r] > m[r - 1])
      if (direct_l == direct_r):
         r = (r+l) // 2
      else: 
         l = (r+l) // 2
   else:
      l = (r+l) // 2 
        
   #print(l, r)
   #time.sleep(0.5)
   return func_ect_right (l, r)


p, tmp = func_ect_right(q, r)
p = p+1
#print('Найден второй экстремум', p)

#print(q, p, len(m)-1)

if m[0] < m[q]:
    list_ekstremum_up.add(0)
    list_ekstremum_up.add(q)
elif m[0] > m[q]:
    list_ekstremum_down.add(0)
    list_ekstremum_down.add(q)

if m[q] < m[p]:
    list_ekstremum_up.add(p)
    list_ekstremum_up.add(q)
elif m[q] > m[p]:
    list_ekstremum_down.add(p)
    list_ekstremum_down.add(q)

if m[p] < m[len(m)-1]:
    list_ekstremum_up.add(len(m)-1)
    list_ekstremum_up.add(p)
elif m[p] > m[len(m)-1]:
    list_ekstremum_down.add(len(m)-1)
    list_ekstremum_down.add(p)

list_ekstremum_up = sorted(list_ekstremum_up)
list_ekstremum_down = sorted(list_ekstremum_down)

list_up = []
for i in range(0, len(list_ekstremum_up), 2):
   list_up.append((list_ekstremum_up[i], list_ekstremum_up[i + 1]))

list_down = []
for i in range(0, len(list_ekstremum_down), 2):
   list_down.append((list_ekstremum_down[i], list_ekstremum_down[i + 1]))


def binary_search_up(l, r, v):
   r += 1
   while (l + 1 < r):
      mid = (l + r) // 2
      if (m[mid] > v):
         r = mid
      else:
         l = mid
   
   # print(f'b{l + 1}', end=' ')
   return m[l] == v


def binary_search_down(l, r, v):
   r += 1
   while (l + 1 < r):
      mid = (l + r) // 2
      if (m[mid] < v):
         r = mid
      else:
         l = mid
   
   # print(f'b{l + 1}', end=' ')
   return m[l] == v

find = [(v, False) for v in find]

# print(m.requests)
# print('-' * 50)
for i in range(len(find)):
   v, f = find[i]
   for l, r in list_up:
      found = binary_search_up(l, r, v)
      # print(found)
      f |= found
      if f:
         break
   
   if f:
      continue

   for l, r in list_down:
      found = binary_search_down(l, r, v)
      # print(found)
      f |= found
      if f:
         break

sys.stdout.write(f'0\n')
sys.stdout.flush()
# print(m.requests)
# 1 2 3 4 5 6 7
# 6 9 8 5 3 1 2

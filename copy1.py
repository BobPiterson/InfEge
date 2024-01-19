
import time 
#m = (88, 90, 91, 92, 93, 100, 95, 89, 87, 77, 76, 61, 60, 49, 45, 40, 12, 9, 3, 6, 8, 11, 19, 24, 33, 65, 67, 70, 73, 82)
#m = (100, 95, 89, 87, 77, 76, 61, 60, 49, 45, 40, 12, 9, 3)
# m = (100, 95, 89, 87, 77, 76, 61, 60, 49, 45, 40, 12, 9, 3, 6, 8, 11, 19, 24, 33, 65, 67, 70, 73, 82)

class MyList(list):
    def __setitem__(self, idx):
        print(idx)


# 
m = (88, 90, 91, 92, 93, 100, 95, 89, 87, 77, 76, 61, 60, 49, 45, 40, 12, 9, 3)

#print (m)
#print(len(m))

if len(m) < 6:
    # Вывести элементы вручную
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


print (sorted(list_ekstremum_up))
print (sorted(list_ekstremum_down))






exit()





        
   
    







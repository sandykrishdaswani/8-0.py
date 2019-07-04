s1,h4=map(int,input().split())
ms=1
while(m<=s1 and m<=h4):
 if(s1%ms==0 and h4%ms==0):
  gd=m
 m=m+1
print(gd)

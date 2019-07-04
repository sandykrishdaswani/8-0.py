ge1,se1=map(int,input().split())
maxima=max(ge1,se1)
while(1):
 if(maxima%ge1==0 and maxima%se1==0):
  print(maxima)
  break
 maxima+=1

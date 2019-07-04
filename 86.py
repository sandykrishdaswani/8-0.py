gif=list(input())
hx=[]
for i in gif:
 if i not in hx:
  hx.append(i)
if(gif==hx):
 print("Yes")
else:
 print("No")

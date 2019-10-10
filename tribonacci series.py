def trib(a):
  if a==0:
    return 1
  elif a==1:
    return 1
  elif a==2:
    return 2
  else:
    return trib(a-1)+trib(a-2)+trib(a-3)

n = int(input("Enter no. of terms you want"))
for i in range(1,n)
  print(trib(i), end=",")

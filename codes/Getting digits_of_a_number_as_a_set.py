ar=[]
def digits():
  n=int(input("Enter the number : Should be greater than 10 "))
  if n<10:
    print("Wrong input!!")
  n=abs(n)
  while n > 0:
    p=int(n%10)
    ar.append(p)
    n=n//10
  return ar
set=digits()
set.reverse()
print(set)

n=int(input("enter the number"))
i=1
x=0
while n % 2 != 0:
    print("It is not a even number")
    break

while i <= n:
    if i % 2 == 0:
        x += i
    i += 1
print(x)
          

        
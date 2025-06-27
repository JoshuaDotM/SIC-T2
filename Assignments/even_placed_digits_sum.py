 #Find sum of the Even placed digits in the given number.
number=input("Enter the number : ")
size=len(number)
sum=0
for i in range(size):
    if i%2==0:
        sum+=int(number[i])
print(sum)

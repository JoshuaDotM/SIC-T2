number=input('Enter a number : ')
prime_list=[2,3,5,7]
count=0
for i in number:
    num=int(i)
    if num in prime_list:
        count+=1
print('The number of prime digits in the number are : ',count)

number=input("Enter your number : ")
digit_list=[]
for i in number:
    digit_list.append(i)
#first find the smallest digit for reference
smallest=int(digit_list[0])
for i in digit_list:
    if smallest>int(i):
        smallest=int(i)
print("The smallest number is : ",smallest)
second_smallest=None
for i in digit_list:
    num=int(i)
    if num > smallest:
        if second_smallest is None or num < second_smallest:
            second_smallest = num
print("The second smallest number is ", second_smallest)
    
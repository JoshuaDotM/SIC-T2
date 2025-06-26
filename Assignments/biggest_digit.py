number=int(input("Enter the number : "))
digits_list=[]
max=0
for i in str(number):
    if int(i) > max:
        max=int(i)
print("The largest digit is ",max)

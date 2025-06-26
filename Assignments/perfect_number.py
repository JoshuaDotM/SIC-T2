number=int(input("Enter a number : "))
digit_list=[]
for i in range(1,number):
    if number%i==0:
        digit_list.append(i)
    else:
        pass
if number==sum(digit_list):
    print("It is a perfect number.")


#footnote- The question was only to find whether a number is perfect,nothing more and nothing less. Avoid adding self interpreted conditions to it.
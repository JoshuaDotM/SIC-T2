#Find sum of the series n - n2/3 + n4/5 - n8/7 .... m terms (1<=n<=4 and 2<=m<=10)
n_value=int(input("Enter the value of n : "))
number_of_terms=int(input("Enter the number of terms required: "))
sum=0
if n_value >= 1 and n_value <= 4 and number_of_terms >= 2 and number_of_terms <=10: 
    for i in range(number_of_terms):
        sign=(-1)**i
        denominator=2*i+1
        sum+=((n_value**2**i)/denominator)*sign
print(sum)
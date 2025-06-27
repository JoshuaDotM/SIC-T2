#Print the Prime numbers in decreasing order between m and n (m < n)
starting_range=int(input('Enter the starting range : '))
ending_range=int(input('Enter the ending range : '))
for i in range(ending_range,starting_range-1,-1):
    if i%2!=0 and i>1:
        print(i)
def partition():
    n, x, y = map(int,input().split())
    sequence_of_integers=(list(map(int,input('Enter the list of numbers : ').split())))
    sequence_of_integers.sort(reverse=True)
    x_array_last_element=sequence_of_integers[n/2]
    y_array_first_element=sequence_of_integers[n/2 + 1]
    p_elements=[]
    temp_list=[]
    temp_list_2=[]
    p_elements=[i for i in temp_list[j for j in range y_array_first_element] - temp_list_2[j for j in range x_array_last_element+1] ]
    return len(p_elements)     


    
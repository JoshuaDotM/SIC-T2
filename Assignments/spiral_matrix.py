def spiral():
    rows = int(input("Enter the dimension : "))
    elements=int(input("Enter the number of elements : "))
    for i in range rows:
        temp = list(int(input(f"Enter the elements of the {rows + 1} row :")))
        if len(temp) > elements:
            
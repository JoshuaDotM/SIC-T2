def memory_allocation():
    numOfReq = int(input("Enter the number of requests to be made: "))
    req = list(map(int, input("Enter the requests separated by spaces: ").split()))
    
    memo_allocation = []
    memo_deallocation = []
    
    if len(req) == numOfReq:
        # Assume even indexed requests are allocations, odd indexed are deallocations
        for i in range(numOfReq):
            if i % 2 == 0:
                memo_allocation.append(req[i])
            else:
                memo_deallocation.append(req[i])
    else:
        print("Number of requests entered does not match the specified number.")
        return
    
    print(f'The number of units under server 1 for memory allocation is {len(memo_allocation)}')
    print(f'The number of units under server 1 for memory de-allocation is {len(memo_deallocation)}')

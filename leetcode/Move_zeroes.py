def move_zeros(arr):
    # zero_counter = 0
    # for i in range(len(arr)):
    #     if arr[i] == 0:
    #         zero_counter += 1
    #     elif zero_counter:
    #         arr[i - zero_counter], arr[i] = arr[i], arr[i - zero_counter]
    # print(arr)

    # explanation
    # if element is not equal to zero move it to start increament j
    # again run a loop from j to len of array and add zeros
    j=0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j+=1
    for i in range(j,len(arr)):
        arr[i]=0
    print(arr)


arr = [0,1,0,3,12]
move_zeros(arr)
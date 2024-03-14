##This function takes an array and a position and input and returns the smallest element that would appear at kth Position
##if the array is [3, 1, 4, 2, 5] and k is 2, then the kth smallest element is 2 because 2 is the second smallest element in the array.
def kth_smallest(temp,pos):          ##Funcation Definition
    temp.sort()                      ##Sorting the array
    if pos<=0:                       ##Checking for condition if the position requested is greater than zero if not returning the first element
        return temp[0]          
    return int(temp[pos-1])

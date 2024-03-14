def remove_duplicates(temp):
    # Get the length of the input array
    len_arr = len(temp)
    # Create an empty array to store unique elements
    rmv_dup = np.empty([], dtype=int)
    # Iterate through the input array
    for i in range(len_arr):
        # Check if the current element is not already in the array of unique elements
        if temp[i] not in rmv_dup:
            # Append the current element to the array of unique elements
            rmv_dup = np.append(rmv_dup, temp[i])
    # Return the array of unique elements
    return rmv_dup


##PS: there is a simple way ----P
rmv_dup=np.unique(arr_name) 

##Import numpy 

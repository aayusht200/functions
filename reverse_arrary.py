def rever_arr(temp):
    # Get the length of the input array
    len_arr = len(temp)
    # Create an empty array to store the reversed elements
    reverse_arr = np.empty((0,), dtype=int)
    # Iterate through the input array in reverse order
    for i in range(len_arr):
        # Decrement the length of the array in each iteration to access elements in reverse order
        len_arr = len_arr - 1
        # Append the element at the current position to the reversed array
        reverse_arr = np.append(reverse_arr, temp[len_arr])
    # Return the reversed array
    return reverse_arr

##there is an easier way ----P
print(arr_name[::-1])

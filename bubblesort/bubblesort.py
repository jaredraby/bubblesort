# Jared Raby 2016
# Bubblesort Implementation in python.
# Reading in an array and sorting it.

def bubblesort(array):
    Array = array
    a = None
    b = None
    i = 0
    loopflag = 1;

    # Outer loop for tracking the overall order of the list. If the flag is set, it will continue to loop
    # through the inner while loop. The inner loop runs through the entire length of the array checking if
    # an element is greater than the element after it. If a swap is made, the flag is set, indicatiing at
    # least 1 more loop is necessary to ensure 100% order.
    while(loopflag == 1):
        # Index tracking for looking at array elements
        i = 0
        # Determines if the outloop should loop. A change in inner loop means at least 1 more loop to
        # verify that the list is ordered
        loopflag = 0
        # While loop that will continue as long as the tracking index is the length of the input array - 1.
        # It's length - 1 to account for the fact that the sort algorithm uses paris of elements at a time
        while(i < len(Array)-1):
            
            # Set the elements to working variables
            a = Array[i]
            b = Array[i+1]
            
            # Checks if the indexed element is bigger than the element after it
            if (a > b):
                # If it is bigger, swap the two elements and set the loopflag to 1, signaling there was a
                # swap in the inner loop, and there needs to be at least 1 more outer loop to verify the 
                # proper array order
                Array[i+1] = a
                Array[i] = b
                loopflag = 1

            # Increment the tracking index to move onto the next pair of elements.
            i = i + 1

    # Return the completed and ordered array
    return Array


# bubblesort
Python implementation of bubblesort

**Requirements**

Bubblesort is a sorting algorithm which looks through an entire array, 2 indices at at time. It sorts the values by looking at each pair of indices. If the array values are in descending order, the values are swapped, otherwise they demain untouched.  

Ethan likes big butts and cannot lie.

**Functionality**

bubblesort(array)
    Set 3 variables: 1 for first object value, 1 for 2nd object value, 1 for the tracking index
    loop while the index is < size
        Read the first 2 values of the array. 
        Do a compare of the two values
        See if n is greater or less than n+1
        If it is, swap the values at their respective locations
        Push the respective indices back into the array
    end loop
    return sorted array
    

**Use**

In python console enter the follow commands:

  * `from bubblesort import bubblesort`
  * `bubblesort(<array of your choice>)`

Sorted array will be returned.



# bubblesort
Python implementation of bubblesort

**Requirements**

Bubblesort is a sorting algorithm which looks through an entire array, 2 indices at at time. It sorts the values by looking at each pair of indices. If the array values are in descending order, the values are swapped, otherwise they demain untouched.  

Ethan likes big butts and cannot lie.

**Functionality**

bubblesort(array)  
  * Set 4 variables: 
    * Outerloop tracking
    * Innerloop (index) tracking
    * A and B for the n and n + 1 index values.
  
  * Outer loop: While loopflag = 1 loop
    * set loopflag and index to 0
    * loop while the index  is < size-1
      * Read in 2 values based on the index and index+1 of the array. 
      * Do a compare of the two values
      * See if n is greater than n+1
      * If it is, swap the values at their respective locations
        * Push the respective indices back into the array
        * Set the loop flag signaling at least 1 more pass is needed to check the loop
      * Increment the index by 1 to check the next 2 values in the list
      * end innerloop
  * End outer loop
  * return sorted array
    

**Use**

In python console enter the follow commands:

  * `from bubblesort import bubblesort`
  * `bubblesort(<array of your choice>)`

Sorted array will be returned.



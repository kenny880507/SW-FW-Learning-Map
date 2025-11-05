def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    ##################
    # YOUR CODE HERE #
    ##################
    n = len(A)
    n_max = 0
    n_current = 0
    for i in range(n):
        if i == 0:
            n_max += 1
            n_current += 1
            continue
        
        if A[i]>A[i-1]:
            n_current += 1
        else:
            n_current = 1
        
        if n_current > n_max:
            n_max = n_current
            count = 1
        elif n_current == n_max:
            count += 1
    
    return count

def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []
    ##################
    # YOUR CODE HERE #
    ##################
    cvt2FTind = lambda x: ord(x)-ord('a')
    T_sub = dict()
    k = len(S[0])
    n = len(T)
    frequency_table = string2FT(T[0:k])
    first_char = T[0]
    key = tuple(frequency_table)
    T_sub[key] = 1
    
    for i in range(1,n-k+1):
        frequency_table[cvt2FTind(first_char)] -= 1
        first_char = T[i]
        frequency_table[cvt2FTind(T[i+k-1])] += 1
        key = tuple(frequency_table)
        if key in T_sub:
            T_sub[key] += 1
        else:
            T_sub[key] = 1
    
    for s in S:
        key = tuple(string2FT(s))
        if key in T_sub:
            A.append(T_sub[key])
        else:
            A.append(0) 
    return tuple(A)

def string2FT(S):
    frequency_table = [0]*26
    cvt2FTind = lambda x: ord(x)-ord('a')
    for s in S:
        frequency_table[cvt2FTind(s)] += 1
    return frequency_table
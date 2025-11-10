def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    B = []
    ##################
    # YOUR CODE HERE #
    ##################
    if len(R)==1:
        s,t = R[0]
        return ((1,s,t),)
    
    n = len(R)//2
    R1 = R[:n]
    R2 = R[n:]
    B = merge(satisfying_booking(R1),satisfying_booking(R2))
    return tuple(B)


def merge(B1,B2):
    n1,n2 = len(B1),len(B2)
    i1,i2 = 0,0
    x = 0
    B = []
    while (i1+i2)<n1+n2:
        if i1<n1:
            k1,s1,t1 = B1[i1]
        else:
            k1,s1,t1 = 0,float('inf'),float('inf')
        if i2<n2:
            k2,s2,t2 = B2[i2]
        else:
            k2,s2,t2 = 0,float('inf'),float('inf')
            
        if i1==n1:
            k,s,t = k2,max(x,s2),t2
            i2 += 1
        elif i2==n2:
            k,s,t = k1,max(x,s1),t1
            i1 += 1
        else:
            if x<min(s1,s2):
                x = min(s1,s2)
            if t2<=s1:
                k,s,t = k2,s2,t2
                x = t2
                i2 += 1
            elif t1<=s2:
                k,s,t = k1,s1,t1
                x = t1
                i1 += 1            
            elif x<s2:
                k,s,t = k1,s1,s2
                x = s2
            elif x<s1:
                k,s,t = k2,s2,s1
                x = s1
            else:
                k,s,t = k1+k2,x,min(t1,t2)
                x = min(t1,t2)
                if x==t1:
                    i1 += 1
                if x==t2:
                    i2 += 1   
        B.append((k,s,t))
    
    B_ = [B[0]]
    for k,s,t in B[1:]:
        k_,s_,t_ = B_[-1]
        if k==k_ and t_==s:
            B_.pop()
            s = s_
        B_.append((k,s,t))
    return B_
            
        
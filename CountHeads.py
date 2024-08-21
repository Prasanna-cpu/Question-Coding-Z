from math import comb

def count_heads(N,R):
    probability=comb(N,R)*(0.5**N)
    return probability



print(count_heads(4,3))
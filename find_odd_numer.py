def find_it(seq):
    odd_n=None
    for x in seq:
        n=seq.count(x)
        if n%2 !=0:
            odd_n=x
    return odd_n

def find_it2(seq):
    return [x for x in seq if seq.count(x)%2!=0][0]


if __name__ == '__main__':
    sqe=[20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
    print(find_it2(sqe))


def accum_test(s):
    counter = 0
    for l in s:
        if counter == 0:
            str1 = l.upper()+'-'
        elif counter<len(s)-1:
            str1 = str1 + l.upper()+l.lower()*counter+'-'
        else:
            str1 = str1 + l.upper()+l.lower()*counter
        counter +=1
    return str1

def accum(s):
    return '-'.join(l.upper()+l.lower()*idx for idx,l in enumerate(s))

def test1(s):
    for idx,l in enumerate(s):
        print(idx,l)

if __name__ == '__main__':
    # print(len(accum_test('ZpglnRxqenU')))
    # print(len(accum('ZpglnRxqenU')))
    # print(accum_test('ZpglnRxqenU'))
    print(accum('ZpglnRxqenU'))
    #test1('ZpglnRxqenU')
# accum("abcd") -> "A-Bb-Ccc-Dddd"


def longest(a1, a2):
    str1=''
    for l in (a1+a2):
        if not (l in str1):
            str1=str1+l
    return ''.join(sorted(str1))


def longest2(a1, a2):
    str1=''
    return str1.join(sorted(str1.join(str1,l)) for l in (a1+a2) if not l in str1)

def longest3(a1, a2):
    return ''.join(sorted(set(a1+a2)))

if __name__ == '__main__':
    print(longest3("aretheyhere", "yestheyarehere"))

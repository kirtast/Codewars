


def anagrams(word,words):
    reference = ''.join(sorted(word))
    result = list()

    for w in words:
        if (''.join(sorted(w)) == reference):
            result.append(w)
    return result

def anagrams2(word,words):
    return [w for w in words if (''.join(sorted(w)) == ''.join(sorted(word)))]




if __name__ == '__main__':
    print(anagrams2('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

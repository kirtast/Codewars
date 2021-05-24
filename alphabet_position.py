from string import ascii_lowercase

def alphabet_position(text):
    return ' '.join(str(ascii_lowercase.index(n.lower())+1) for n in text if n.isalpha())

if __name__ == '__main__':
    print(alphabet_position('Jose'))

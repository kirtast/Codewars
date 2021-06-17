
import re
def spin_words(sentence):
    # for word in re.split(' ',sentence):
    #     print(word)
    return ' '.join([''.join(word) if len(word)<5 else ''.join(reversed(word)) for word in re.split(' ',sentence)])



if __name__ == '__main__':
    print(spin_words('Hey fellow warriors'))

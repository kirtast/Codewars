def to_camel_case(text):
    import re
    return ''.join([text[i].upper() if i-1 in ([chr.start() for chr in re.finditer('_',text)] + \
     [chr.start() for chr in re.finditer('-',text)]) else text[i] if i in [idx for idx,chr in enumerate(text) if chr==text[idx].upper()] else text[i].lower() \
     for i in range(len(text))]).replace('_','').replace('-','')

def to_camel_case2(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)
def to_camel_case4(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s
if __name__ == '__main__':
    print(to_camel_case('The_stealth-warrior'))

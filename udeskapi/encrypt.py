import hashlib
import random

##md5加密算法
def create_md5(str):
    b = hashlib.md5()
    b.update(str.encode(encoding='utf-8'))
    sign = b.hexdigest()
    return sign


##SHA256加密算法
def create_SHA256(str):
    b = hashlib.sha256()
    b.update(str.encode(encoding='utf-8'))
    sign = b.hexdigest()
    return sign

##SHA1加密算法
def create_SHA1(str):
    b = hashlib.sha1()
    b.update(str.encode(encoding='utf-8'))
    sign = b.hexdigest()
    return sign

def createRandomString(len):

    raw = ""
    range1 = range(58, 65) # between 0~9 and A~Z
    range2 = range(91, 97) # between A~Z and a~z

    i = 0
    while i < len:
        seed = random.randint(48, 122)
        if ((seed in range1) or (seed in range2)):
            continue;
        raw += chr(seed);
        i += 1
    # print(raw)
    return raw

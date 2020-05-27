import hashlib

##md5加密算法
def create_md5(str):
    b = hashlib.md5()
    b.update(str.encode(encoding='utf-8'))
    sign = b.hexdigest()
    return sign


##SHA1加密算法
def create_SHA1(str):
    b = hashlib.sha1()
    b.update(str.encode(encoding='utf-8'))
    sign = b.hexdigest()
    return sign

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def CBC():
    # get aes key
    aes_key = get_random_bytes(16)
    cipher = AES.new(aes_key, AES.MODE_CTR)

    



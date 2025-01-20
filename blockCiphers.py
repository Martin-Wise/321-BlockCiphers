#pip install pycyptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# ECB Mardy
def ECB(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext : bytes = b''
    for index in range(16, len(plaintext), 16):
        block = plaintext[index-16:index]
        print("b", block)
        ciphertext += cipher.encrypt(block)
    return ciphertext


# CBC Melika
def CBC(plaintext, key, iv):
    print("temp")
    aes_key = get_random_bytes(16)
    cipher = AES.new(aes_key, AES.MODE_CTR)

def add_padding(plaintext : bytes, blocksize=16):
    byte_length = len(plaintext)
    pad_number = blocksize - byte_length % blocksize
    return plaintext + bytes([pad_number]) * pad_number 

def task1():
    
    # import the file
    with open("mustang.bmp", "rb") as file:
        plaintext = file.read()
        # remove the header
        header = plaintext[:54]
        plaintext = plaintext[54:]
            
        #add padding to make the plaintext in 16 byte blocks
        plaintext = add_padding(plaintext, blocksize=16)


        #create key and iv
        key = get_random_bytes(16)
        iv = get_random_bytes(16)

        #encrypt the plaintext
        ciphertext1 = ECB(plaintext, key)
        # ciphertext2 = CBC(plaintext, key, iv)

        # add the header
        cypherfile1raw = header + ciphertext1

        # save as new files
        with open("mustangECB.bmp", "wb") as cipherfile1:
            cipherfile1.write(cypherfile1raw)
        


task1()
        
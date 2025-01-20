#pip install pycyptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# ECB Mardy
def ECB(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext : bytes = b''
    for index in range(0, len(plaintext), 16):
        block = plaintext[index:index+16]
        # print("b", block)
        ciphertext += cipher.encrypt(block)
    return ciphertext


# CBC Melika
def CBC(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_ECB) # still picking ecb mode for manual implementation
    ciphertext: bytes = b''
    prev_block = iv

    for index in range(16, len(plaintext), 16):
        block = plaintext[index-16:index]
        # XOR the block with the previous ciphertext block 
        xored_block = bytes([b1 ^ b2 for b1, b2 in zip(block, prev_block)]) 
        encrypted_block = cipher.encrypt(xored_block)
        ciphertext += encrypted_block
        prev_block = encrypted_block

    return ciphertext    


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
        ciphertext2 = CBC(plaintext, key, iv)

        # add the header
        cipherfile1raw = header + ciphertext1
        cipherfile2raw = header + ciphertext2

        # save as new files
        with open("mustangECB.bmp", "wb") as cipherfile1:
            cipherfile1.write(cipherfile1raw)

        with open("mustangCBC.bmp", "wb") as cipherfile2:
            cipherfile2.write(cipherfile2raw)

task1()
        
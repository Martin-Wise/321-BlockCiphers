#pip install pycyptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#key and IV
key = get_random_bytes(16)
iv = get_random_bytes(16)



# ECB Mardy
def ECB(plaintext):
    print("temp")

# CBC Melika
def CBC(plaintext):
    print("temp")
    aes_key = get_random_bytes(16)
    cipher = AES.new(aes_key, AES.MODE_CTR)



def task1():
    # import the file
    with open("mustang.bmp", "rb") as file:
        plaintext = file.read()
        # remove the header
        header = plaintext[0:54]
        plaintext = plaintext[54:]
        print(plaintext)
        print(header)

        # add padding 
        
        #encrypt the plaintext
        cyphertext1 = ECB(plaintext)
        ciphertext2 = CBC(plaintext)

        # add the header

        # save as new files

task1()
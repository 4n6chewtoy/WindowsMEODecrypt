####
# A python script designed to take an encrypted .meo file and 
# display the MD5 hash value of the password in order to allow
# bruteforcing using applications such as hashcat
# Original blog post: https://theincidentalchewtoy.wordpress.com/2021/11/09/meo-file-encryption-software/
###

# Import required modules
import sys
from xorCryptPy import xorCrypt

# Take a file input
encryptedFile = sys.argv[1]

# Define keyValue
keyValue = 254

# Open the file for reading
with open (encryptedFile, 'rb') as dataStream:
    # Read the header
    fileHeader = dataStream.read(8)
    # Check its a meo encrypted file
    if fileHeader == b' HCN 0.1':
        # Continue to read file
        # Read from the start of the file until the key length indicator
        dataStream.seek(20,0)
        # Read the key length (32)
        keyLength = dataStream.read(4)
        # Read the key
        key = (dataStream.read(int.from_bytes(keyLength, "little"))).hex()
        # Split the key into chunks
        passwordHashChunks = [key[i:i+2] for i in range(0,len(key),2)]
        # Iterate through the chunks and xor to get original values
        md5hash = ""
        for chunks in passwordHashChunks:
            md5hash = md5hash + (xorCrypt(chr(int(chunks,16)), keyValue))
        # Print the MD5 hash for cracking
        print(f'Your MD5 hash value for the file is: {md5hash}')
        
    else:
        # If the file header is not correct exit
        print("This is not the right file type")
        exit()

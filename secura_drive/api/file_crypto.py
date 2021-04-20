from cryptography.fernet import Fernet


def generateKey():  ## generates a key  store in DB caution is object of bytes type NOT string
    key=Fernet.generate_key()
    return key

def encrypt(original,key): ## encrypts a file and stores (filename) "+_enc" (.ext)
    fernet_obj=Fernet(key)
    
    encrypted = fernet_obj.encrypt(original)
   
    return encrypted


def decrypt(encrypted,key):  ## decrypts a file and stores (filename) "+_dec" (.ext)
    fernet_obj=Fernet(key)
    
    decrypted = fernet_obj.decrypt(encrypted)
    
    return decrypted


# encrypt('1.txt',b'NtEvVBWbzSEBu6axGA21Aw6pt3MsO1zFM_mCu9Al8oM=')

# decrypt('a.txt',b'NtEvVBWbzSEBu6axGA21Aw6pt3MsO1zFM_mCu9Al8oM=')
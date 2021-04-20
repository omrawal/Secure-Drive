from cryptography.fernet import Fernet

def generateKey():  ## generates a key  store in DB caution is object of bytes type NOT string
    key=Fernet.generate_key()
    return key

def encrypt(filename,key): ## encrypts a file and stores (filename) "+_enc" (.ext)
    fernet_obj=Fernet(key)
    with open(filename, 'rb') as original_file:
        original = original_file.read()
    
    encrypted = fernet_obj.encrypt(original)
    newFilename=filename.split('.')
    newFileName='_enc.'.join(newFilename)
    # print(newFileName)
    with open (newFileName, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    return True


def decrypt(filename,key):  ## decrypts a file and stores (filename) "+_dec" (.ext)
    fernet_obj=Fernet(key)
    with open(filename, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = fernet_obj.decrypt(encrypted)
    newFilename=filename.split('_enc.')
    newFileName='_dec.'.join(newFilename)
    # print(newFileName)
    with open(newFileName, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    return True

# Example


# encrypt('1.txt',b'NtEvVBWbzSEBu6axGA21Aw6pt3MsO1zFM_mCu9Al8oM=')

# decrypt('1_enc.txt',b'NtEvVBWbzSEBu6axGA21Aw6pt3MsO1zFM_mCu9Al8oM=')
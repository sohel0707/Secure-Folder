import pyAesCrypt
from os import stat, remove, listdir
import os
bufferSize = 64 * 1024
password = "foopassword"

path = r"C:\Users\SOHEL\Desktop\Secure Folder\secure"
os.chdir(path)
os.mkdir('sohel')

# encrypt
def encrypt(file):
    with open(file, "rb") as fIn:
        with open(file+".aes", "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
    remove(file)
# get encrypted file size


# decrypt
def decrypt(file):
    encFileSize = stat(file+".aes").st_size
    with open(file+".aes", "rb") as fIn:
        try:
            with open(file, "wb") as fOut:
            # decrypt file stream
                pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
        except ValueError:
        # remove output file on error
            remove(file)
    remove(file+'.aes')


def listOfFilesEncrypt():
    all_files_folders=listdir(path)
    all_files=[]
    for file in range(len(all_files_folders)):
        all_files_folders[file]=path+'\\'+all_files_folders[file]
        if os.path.isfile(all_files_folders[file]):
            # all_files_folders[file] = '.'.join(all_files_folders[file].split('.')[:-1])
            all_files.append(all_files_folders[file])
    return all_files

def listOfFiles():
    all_files_folders=listdir(path)
    all_files=[]
    for file in range(len(all_files_folders)):
        
        if os.path.isfile(path+'\\'+all_files_folders[file]):
            all_files_folders[file] = '.'.join(all_files_folders[file].split('.')[:-1])
            all_files_folders[file]=path+'\\'+all_files_folders[file]
            all_files.append(all_files_folders[file])
    return all_files


import bluetooth
import time
f=open('is_encrypted.txt','r')
val=f.read()
f.close()
while True:
    mac='94:14:7A:A3:57:BA'
    name="vivo 1714"
    devices=bluetooth.discover_devices(lookup_names=True)
    for address, name1 in devices:
        if address==mac and name1==name:
            print("Device found successfully")

            if val=="1":
                all_files =listOfFiles()
                for file in all_files:
                    decrypt(file)

                val="0"
                f=open('is_encrypted.txt','w')
                f.write(val)
                f.close()
                print("decrypted successfully")
            break
    else:
        if val=="0":
            all_files = listOfFilesEncrypt()
            for file in all_files:
                encrypt(file)
            val="1"
            f=open('is_encrypted.txt','w')
            f.write(val)
            f.close()
            print("excrpted successfully")


    
    exit()  
    time.sleep(5)

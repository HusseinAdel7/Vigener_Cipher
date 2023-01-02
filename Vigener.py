import os.path
from sys import platform
import os 
import string
from termcolor import colored
from Crypto.Cipher import DES3
from Crypto.Util import Counter
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random 
from Crypto.Cipher import DES3


os.system('clear') 

print ("\n\n\t\t\t    ------------------")
print(colored('\t\t\t      Cryptography ', 'yellow'))
print ("\t\t\t    ------------------")
print(colored('\n\t     * Written by : ', 'green'),end="")
print(colored(' Hussein Adel', 'white'),end="")
print ("\n\t\t\t     ------------\n")
print (" ===========================================================================\n")
print (colored('\t\t\t\t  ------------','white'))
print(colored('\t\t\t\t    Hello \U0001f600 ', 'yellow'))
print (colored('\t\t\t\t  ------------\n','white'))
#------------------------------------------------------------------------  
#========================================================================
# Vegener Cipher 

def vigener_Encryption(plain_text,key):
    letter1=string.ascii_lowercase
    letter2=string.ascii_uppercase
    index=0
    cipher_text=""
    for c in plain_text:
         if c in letter1:
            enc_message=chr(((ord(c)-97+(ord(key[index])-97))%26)+97)
            cipher_text+=enc_message
            index=(index+1)%len(key)
         elif c in letter2:
            enc_message=chr(((ord(c)-65+(ord(key[index])-65))%26)+65)
            cipher_text+=enc_message
            index=(index+1)%len(key)
         else:
            cipher_text+=c
    print("plain text: ",plain_text)
    print("cipher text: ",cipher_text)
def vigener_Decryption(cipher_text,key):
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    index=0
    plain_text=""
    key=key
    for c in cipher_text:
         if c in lower:
            keyy=ord(key[index])-97
            dec_message=chr((ord(c)-97+(26-keyy))%26+97)
            plain_text+=dec_message    
            index=(index+1)%len(key)
         elif c in upper:
            keyy=ord(key[index])-65
            dec_message=chr((ord(c)-65+(26-keyy))%26+65)
            plain_text+=dec_message
            index=(index+1)%len(key)
         else:
            plain_text+=c
    print("cipher text: ",cipher_text)
    print("plain text (message): ",plain_text)



choose =int(input(colored("\n1- Encryption\n2- Decryption\n\nChoice '1' or '2': ", 'white')))
if choose ==1:
    plain_Text =str(input(colored("\nEnter Your Message That You Wanna encrypt :  " , 'green')))
    secret_Key= input(colored("Enter The Secret key : " , 'green'))
    vigener_Encryption(plain_Text,secret_Key)

if choose ==2:
    plain_Text =str(input(colored("\nEnter Your Message That You Wanna decrypt :  " , 'green')))
    secret_Key= input(colored("Enter The Secret key : " , 'green'))
    vigener_Decryption(plain_Text,secret_Key)
#---------------------------------------------------------------------------------------
print (colored('\n\n\t\t\t\t  ----------','white'))
print(colored('\t\t\t\t    Done \U0001f600 ', 'yellow'))
print (colored('\t\t\t\t  ----------\n','white'))


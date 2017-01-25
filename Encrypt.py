"""Write a code that will take (AnyString) and substitute all vowels with
character's like $#%^&* etc..... but DO NOT USE ' or " as any of your characters."""

AnyString = 'Encryption is hard but Decryption is even harder'
def Encryption(AnyString):
    #aeiouy
    Encrypt = ""
    AnyString = AnyString.lower()
    CipherSub = '$#%^&*'
    for ch in AnyString:
        if ch == 'a':
            ch = CipherSub[0]
            Encrypt = Encrypt + ch
        elif ch == 'e':
            ch = CipherSub[1]
            Encrypt = Encrypt + ch
        elif ch =='i':
            ch = CipherSub[2]
            Encrypt = Encrypt + ch
        elif ch == 'o':
            ch = CipherSub[3]
            Encrypt = Encrypt + ch
        elif ch =='u':
            ch = CipherSub[4]
            Encrypt = Encrypt + ch
        elif ch =='y':
            ch = CipherSub[5]
            Encrypt = Encrypt + ch
        else:
            Encrypt = Encrypt + ch

    return Encrypt
print (Encryption(AnyString))

plainText = "The lazy Student Never Gets Paid!"
def Encrypt(plainText):
    plainText = plainText.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    number = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26'
    number = number.split()
    CipherText = ""
    for i in plainText:
        if i == ' ':
            CipherText = CipherText + '_'
        else:
            idx = alphabet.find(i)
            CipherText = CipherText + number[idx] + ' '
    return CipherText
print (Encrypt('Any chance i could borrow a dollar until friday'))

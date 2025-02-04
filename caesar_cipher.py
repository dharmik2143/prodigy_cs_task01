#ceaser Cipher
plain_text=input("Enter a text:")
key=int(input("Enter a key:"))
for letter in plain_text:
    if(ord(letter)>96 and ord(letter)<128):
        cipher=(ord(letter)+key)
        cipher=cipher-97
        cipher=cipher%26
        cipher=cipher+97
        print(chr(cipher),end='')
    elif(ord(letter)>64 and ord(letter)<91):
        cipher=(ord(letter)+key)
        cipher=cipher-65
        cipher=cipher%26
        cipher=cipher+65
        print(chr(cipher),end='')
#covert into real text
plain_text=input("Enter a text:")
key=-int(input("Enter a key:"))
for letter in plain_text:
    if(ord(letter)>96 and ord(letter)<128):
        cipher=(ord(letter)+key)
        cipher=cipher-97
        cipher=cipher%26
        cipher=cipher+97
        print(chr(cipher),end='')
    elif(ord(letter)>64 and ord(letter)<91):
        cipher=(ord(letter)+key)
        cipher=cipher-65
        cipher=cipher%26
        cipher=cipher+65
        print(chr(cipher),end='')
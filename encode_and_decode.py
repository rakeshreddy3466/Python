import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text,shift_amount):
    cipher_text = ""
    for x in original_text:
        if direction == "encode":  
            if x in alphabet:  
                a = alphabet.index(x) + shift_amount
                cipher_text += alphabet[a%26]
            else:
                cipher_text += x     
        # print(cipher_text)
        else:
            if x in alphabet:
                a = alphabet.index(x) - shift_amount
                cipher_text += alphabet[a%26]
            else:
                cipher_text += x
    print(cipher_text)   

repeat_again = True
while repeat_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift)
    

    repeat  = input("if you want run again type 'YES' or type 'NO'").lower()
    if repeat == "no":
        repeat_again = False
        print("good bye")  

# we importred the logo from thge art module which is always presented in the file art.py       







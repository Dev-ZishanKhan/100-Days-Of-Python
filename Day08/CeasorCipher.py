
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encryption(originalText,shiftAmount):
    
        encrypted=""
        for letter in originalText:
            shifedIndex=(alphabets.index(letter)+shiftAmount )%26
            encrypted+=alphabets[shifedIndex]
        print("\nHere is Your Encrypted Message: "+ encrypted)

def decryption(encryptedText,shifted):
        decrypted=""
        for letter in encryptedText:
            shifedIndex=(alphabets.index(letter)-shifted)%26
            decrypted+=alphabets[shifedIndex]
        print("\nHere is Your Decrypted Message: "+decrypted)


def CeasorCipher():
    print("************************************************************************")
    choice=input("Type encode for Encryption or decode For decryption: ").lower()
    if choice=="encode":
        print("                                            ")
        orignal=input("Enter Message to Encrypt: ").lower()
        shifts=int(input("\nType Shifts Number: "))
        encryption(originalText=orignal,shiftAmount=shifts)
        again=input("\nType 'Yes' for going again, Otherwise 'No' to exit: ").lower()
        if again=="yes":
             CeasorCipher()
        else:
             print("\nThank you for using our platform......")
             
    elif choice=="decode":
        encrypted=input("\nEnter Text To decrypt: ").lower()
        shifts=int(input("\nEnter Shifts: "))
        decryption(encryptedText=encrypted,shifted=shifts)
        again=input("\nType 'Yes' for going again, Otherwise 'No' to exit: ").lower()
        if again=="yes":
             CeasorCipher()
        else:
             print("\nThank you for using our platform......")
             
    else:
         print("\nInvalid Input..")

CeasorCipher()










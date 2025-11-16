'Caesar cipher techniqe Using Python encryption or decryption'
def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():      
                new = ord(ch) + shift
                if new > ord('Z'):
                    new = new - 26
                result += chr(new)
            else:                
                new = ord(ch) + shift
                if new > ord('a') + 25: 
                    new = new - 26
                result += chr(new)
        else:
            result += ch
    return result


def decrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():     
                new = ord(ch) - shift
                if new < ord('A'):
                    new = new + 26
                result += chr(new)
            else:                
                new = ord(ch) - shift
                if new < ord('a'):
                    new = new + 26
                result += chr(new)
        else:
            result += ch
    return result


print("1 = Encrypt")
print("2 = Decrypt")
choice = int(input("Enter choice: "))
msg = input("Enter text: ")
shift = int(input("Enter shift value: "))

if choice == 1:
    print("Encrypted Text =", encrypt(msg, shift))
elif choice == 2:
    print("Decrypted Text =", decrypt(msg, shift))
else:
    print("Invalid choice")
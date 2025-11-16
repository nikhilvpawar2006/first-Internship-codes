from PIL import Image
def encrypt_img(img_name, key=100):
    img = Image.open(img_name)
    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save("encrypted.png")
    print("Encryption Done → encrypted.png ready!")


def decrypt_img(img_name, key=100):
    img = Image.open(img_name)
    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save("decrypted1.png")
    print("Decryption Done → decrypted.png ready!")



print("1 = Encrypt Image")
print("2 = Decrypt Image")
ch = int(input("Enter Choice: "))

if ch == 1:
    encrypt_img("ph.png")
elif ch == 2:
    decrypt_img("encrypted.png")
else:
    print("Invalid Choice")
from cryptography.fernet import Fernet

# ki = Fernet.generate_key()

# with open('ki.txt', 'wb') as f:
#     f.write(ki)
#     f.close()
key = input('Enter your key: ')

ki = bytes(key.encode())

print(ki)

fer = Fernet(ki)

msg = input('Enter your msg')

with open('enc.txt', 'wb') as f:
    msgenc = fer.encrypt(msg.encode())
    print(msgenc)
    f.write(msgenc)
    print("Write encrypted file")
    f.close()

print("Opened and read from encyrped file")

with open('enc.txt', 'rb') as f:
    lines = f.read()
    dec = fer.decrypt(lines).decode()
    print(dec)
    f.close()

with open('dec.txt', 'w') as f:
    f.write(dec)
    print(dec)
    print("Decrypted printed")
    f.close()
print("Opened and read from", lines)
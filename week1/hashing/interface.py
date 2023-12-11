import tkinter as tk
import hashlib
import tkinter.messagebox as messagebox

def encrypt_message():
    key = key_entry.get()
    message = message_entry.get()

    # Hash the message with SHA256
    hashed_message = hashlib.sha256(message.encode()).digest()
    print(len(key))
    # Encrypt the hashed message using the provided key
    encrypted_message = hashlib.sha256(key.encode() + hashed_message).hexdigest()
    print(encrypted_message)
    # Display the encrypted message
    result_label.config(text=encrypted_message)


def decrypt_message():
    key = key_entry.get()
    encrypted_message = message_entry.get()

    # Decrypt the encrypted message using the provided key
    decrypted_message = hashlib.sha256(key.encode() + bytes.fromhex(encrypted_message)).digest()

    # Display the decrypted message
    result_label.config(text=decrypted_message.decode())

# Create the tkinter window
window = tk.Tk()
window.title("Hashing Interface")

# Create the key entry field
key_label = tk.Label(window, text="Key:")
key_label.pack()
key_entry = tk.Entry(window)
key_entry.pack()

# Create the message entry field
message_label = tk.Label(window, text="Message:")
message_label.pack()
message_entry = tk.Entry(window)
message_entry.pack()

# Create the encrypt button
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_message)
encrypt_button.pack()

# Create the decrypt button
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_message)
decrypt_button.pack()

def decrypt_message():
    key = key_entry.get()
    encrypted_message = message_entry.get()

    # Convert the encrypted message from hex to bytes
    encrypted_bytes = bytes.fromhex(encrypted_message)

    # Extract the key from the encrypted bytes
    extracted_key = encrypted_bytes[:len(key)]

    # Extract the hashed message from the encrypted bytes
    hashed_message = encrypted_bytes[len(key):]

    # Decrypt the hashed message using the provided key
    decrypted_message = hashlib.sha256(key.encode() + hashed_message).digest()

    # Display the decrypted message
    result_label.config(text=decrypted_message.decode())

# Create the label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the tkinter event loop
window.mainloop()

from tkinter import *
import random

# Diffie-Hellman Key Exchange Algorithm

# Alice and Bob agree on a prime number p and a primitive root g
p = 131071
g = 3

# Alice generates a random number a
a = random.randint(2, p-1)

# Bob generates a random number b
b = random.randint(2, p-1)

# Alice computes A = g^a mod p
A = pow(g, a, p)

# Bob computes B = g^b mod p
B = pow(g, b, p)

# Alice and Bob exchange A and B
# Alice receives B and computes s = B^a mod p
s_alice = pow(B, a, p)

# Bob receives A and computes s = A^b mod p
s_bob = pow(A, b, p)

# Both Alice and Bob now have the same shared secret key
shared_key = s_alice
assert(shared_key == s_bob)


# Encryption and Decryption Functions

def encrypt(msg, key):
    # Convert the message to a list of ASCII codes
    ascii_codes = [ord(c) for c in msg]

    # XOR each ASCII code with a character of the key
    key_codes = [ord(c) for c in key]
    key_len = len(key_codes)
    encrypted_codes = [ascii_codes[i] ^ key_codes[i % key_len] for i in range(len(ascii_codes))]

    # Convert the encrypted codes to a string
    encrypted_msg = ''.join([chr(c) for c in encrypted_codes])
    return encrypted_msg


def decrypt(msg, key):
    # Convert the encrypted message to a list of ASCII codes
    encrypted_codes = [ord(c) for c in msg]

    # XOR each ASCII code with a character of the key
    key_codes = [ord(c) for c in key]
    key_len = len(key_codes)
    decrypted_codes = [encrypted_codes[i] ^ key_codes[i % key_len] for i in range(len(encrypted_codes))]

    # Convert the decrypted codes to a string
    decrypted_msg = ''.join([chr(c) for c in decrypted_codes])
    return decrypted_msg


# GUI

def encrypt_message():
    msg = plaintext_entry.get()
    key = str(shared_key)
    encrypted_msg = encrypt(msg, key)
    ciphertext_entry.delete(0, END)
    ciphertext_entry.insert(0, encrypted_msg)


def decrypt_message():
    msg = ciphertext_entry.get()
    key = str(shared_key)
    decrypted_msg = decrypt(msg, key)
    plaintext_entry.delete(0, END)
    plaintext_entry.insert(0, decrypted_msg)


root = Tk()
root.title("Diffie-Hellman Encryption")
root.geometry("800x400")
root.configure(background="#2c3e50")
root.option_add("*foreground", "white") # set the size of the window



plaintext_label = Label(root, text="Plaintext:", font=("Arial", 14), bg="#2c3e50", fg="white")
plaintext_label.grid(row=0, column=0, padx=10, pady=10)

plaintext_entry = Entry(root, width=40, font=("Arial", 14), bg="#e8f8f5", fg="#2c3e50")
plaintext_entry.grid(row=0, column=1, padx=10, pady=10)

ciphertext_label = Label(root, text="Ciphertext:", font=("Arial", 14), bg="#2c3e50", fg="white")
ciphertext_label.grid(row=1, column=0, padx=10, pady=10)

ciphertext_entry = Entry(root, width=40, font=("Arial", 14), bg="#e8f8f5", fg="#2c3e50")
ciphertext_entry.grid(row=1, column=1, padx=10, pady=10)

encrypt_button = Button(root, text="Encrypt", command=encrypt_message, width=20, font=("Arial", 10), bg="#e8f8f5", fg="#2c3e50")
encrypt_button.grid(row=2, column=0, padx=5, pady=5)

decrypt_button = Button(root, text="Decrypt", command=decrypt_message, width=20, font=("Arial", 10), bg="#e8f8f5", fg="#2c3e50")
decrypt_button.grid(row=2, column=1, padx=5, pady=5)

quit_button = Button(root, text="Quit", command=root.quit, width=20, font=("Arial", 10), bg="#e8f8f5", fg="#2c3e50")
quit_button.grid(row=2, column=2, padx=5, pady=5)

root.mainloop()
